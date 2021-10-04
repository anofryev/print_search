# Выкачиваем из dockerhub образ с python версии 3.9
FROM python:3.8.10

# author
MAINTAINER Anofryev Alex
# Устанавливаем рабочую директорию для проекта в контейнере
WORKDIR /backend
# Скачиваем/обновляем необходимые библиотеки для проекта
COPY requirements.txt /backend
#Требования для питоновского апи:
RUN pip3 install --upgrade pip -r requirements.txt
RUN apt-get update ##[edited]
RUN apt-get install ffmpeg libsm6 libxext6  -y

#Требования для тессеракта
RUN apt update
RUN apt-get install -y automake ca-certificates g++ git libtool libleptonica-dev make pkg-config

# |ВАЖНЫЙ МОМЕНТ| копируем содержимое папки, где находится Dockerfile,
# в рабочую директорию контейнера
COPY . /backend

# Распаковываем и устанавливаем тессеракт с отключеным openMP (multiprocessing)
WORKDIR ./tesseract
RUN ls
RUN tar -xvzf tesseract-4.0.0.tar.gz
WORKDIR ./tesseract-4.0.0
RUN ls
RUN ./autogen.sh
WORKDIR ./bin/release

RUN ../../configure --disable-openmp --disable-shared 'CXXFLAGS=-g -O2 -fno-math-errno -Wall -Wextra -Wpedantic'
RUN make
WORKDIR ../../../../

# Копируем языковые модели
COPY ./tesseract_models/. /usr/share/tesseract-ocr/4.00/tessdata/

# Устанавливаем порт, который будет использоваться для сервера
EXPOSE 5000
CMD python3 app.py

#sudo docker run -p 5000:5000 -v /usr/archive_scans/:/usr/archive_scans/ -v /home/alex/PycharmProjects/Prints_search/configs:/backend/configs my_image

#sudo docker run -p 5000:5000 -v /opt/storage/wstorage/:/opt/storage/wstorage/ -v /home/nahodka-anofryev/search_api_docker/configs:/backend/configs search__flask