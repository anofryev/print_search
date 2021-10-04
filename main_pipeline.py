import threading

import cv2
from PIL import Image
from tesserocr import PyTessBaseAPI, RIL
import time
from functools import partial
from sqlalchemy import and_
from multiprocessing.pool import ThreadPool

import os
from configs import config

from models import Sourcearchive, Property, Sheet, Word

def search_main(archive_ids_list, words_to_find_list, session, sheet_ids_list=None):
    print("words_to_find_list: ", words_to_find_list)
    content = {}
    start_time = time.time()

    base_path = session.query(Property.propertyvalue).filter(
        Property.propertykey == "source.documentBasePath").first()[0]
    for archive_id in archive_ids_list:
        if sheet_ids_list is None:
            sheets = session.query(Sheet).filter(Sheet.source_id == archive_id).order_by(Sheet.number).all()
        else:
            sheets = session.query(Sheet).filter(and_(
                Sheet.source_id == archive_id, Sheet.id.in_(sheet_ids_list))).order_by(Sheet.number).all()

        print("sheets: ", sheets)
        # мультитрединг
        sheet_processing_partial = partial(sheet_processing, base_path=base_path,
                                           words_to_find_list=words_to_find_list)


        pool = ThreadPool(processes=config.NUMBER_OF_THREADS)
        finded_words_by_sheets_list = pool.map(sheet_processing_partial, sheets)
        pool.close()
        pool.join()

        # Words упакованы по шитам, распакуем в один список.
        words_list = [word for words in finded_words_by_sheets_list for word in words]

        archive_dict = get_archive_dict(words_list=words_list, archive_id=archive_id)
        content[archive_id] = archive_dict
    print(content)
    print('Время работы функции: {}'.format(time.time() - start_time))
    session.commit()
    return content

def sheet_processing(sheet, base_path, words_to_find_list):
    image_path = base_path + "/" + sheet.scanfilepath
    img = cv2.imread(image_path, 0)
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    img = clahe.apply(img)
    img = cv2.bilateralFilter(img, 15, 80, 80)
    img_pil = Image.fromarray(img)
    with PyTessBaseAPI(psm=1, oem=1, lang=config.MODEL_NAME) as api:
        api.SetImage(img_pil)

        api.SetVariable("language_model_penalty_non_freq_dict_word", "1")
        api.SetVariable("language_model_penalty_non_dict_word", "1")

        level = RIL.WORD
        api.Recognize()
        finded_words_list = []
        ri = api.GetIterator()
        while (ri.Next(level)):
            text = ri.GetUTF8Text(level)
            print(text)
            boxes = ri.BoundingBox(level)
            for word_to_find in words_to_find_list:
                if word_to_find in text.lower():
                    (x1, y1, x2, y2) = boxes
                    word = Word(
                        x=x1,
                        y=y1,
                        h=y2-y1,
                        w=x2-x1,
                        sheet_id=sheet.id,
                        archive_id=sheet.source_id,
                        word=text
                    )

                    finded_words_list.append(word)
    print()
    return finded_words_list

def get_archive_dict(words_list, archive_id):
    print("words_list: ", words_list)

    sheets = {}
    for index, word in enumerate(words_list):
        print(word.to_dict())
        if word.sheet_id not in sheets:
            sheets[word.sheet_id] = {
                "sheet_id": word.sheet_id,
                "words": {index: word.to_dict()}
            }
        else:
            sheets[word.sheet_id]["words"].update({index: word.to_dict()})
    print("sheets: ", sheets)
    archive_dict = {"archive_id": archive_id,
                    "sheets": sheets
                    }
    return archive_dict
