# coding: utf-8
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgresql import UUID


db = SQLAlchemy()


class Word:

    def __init__(self, x,y,h,w, sheet_id, archive_id, word):
        self.x = x
        self.y = y
        self.h = h
        self.w = w
        self.sheet_id = sheet_id
        self.archive_id = archive_id
        self.word = word


    def to_dict(self):
        finding_dict = {
            "x": self.x,
            "y": self.y,
            "h": self.h,
            "w": self.w,
            "word_text": self.word
        }
        return finding_dict
# ==================================================================================================================


class Accountrequest(db.Model):
    __tablename__ = 'accountrequest'

    id = db.Column(db.BigInteger, primary_key=True)
    additional = db.Column(db.String(1000))
    changestatusdate = db.Column(db.DateTime)
    email = db.Column(db.String(255), nullable=False, unique=True)
    firstname = db.Column(db.String(255), nullable=False)
    lastname = db.Column(db.String(255), nullable=False)
    organization = db.Column(db.String(255))
    password = db.Column(db.String(255))
    patronymic = db.Column(db.String(255))
    phone = db.Column(db.String(255), nullable=False)
    post = db.Column(db.String(255))
    regrequeststatus = db.Column(db.Integer)
    requestdate = db.Column(db.DateTime)
    requesttype = db.Column(db.Integer)
    uuid = db.Column(db.String(255))



class Addres(db.Model):
    __tablename__ = 'address'

    id = db.Column(db.BigInteger, primary_key=True)
    city = db.Column(db.String(255))
    citytype = db.Column(db.String(255))
    country = db.Column(db.String(255))
    district = db.Column(db.String(255))
    districttype = db.Column(db.String(255))
    region = db.Column(db.String(255))
    regiontype = db.Column(db.String(255))
    town = db.Column(db.String(255))
    towntype = db.Column(db.String(255))



class AdminSheetsByStatu(db.Model):
    __tablename__ = 'admin_sheets_by_status'

    sheet_id_max = db.Column(db.BigInteger, primary_key=True, nullable=False)
    sheet_id_min = db.Column(db.BigInteger, primary_key=True, nullable=False)
    status = db.Column(db.Integer, primary_key=True, nullable=False)
    act = db.Column(db.Integer)
    actletter = db.Column(db.String(255))
    count = db.Column(db.Integer)
    firstname = db.Column(db.String(255))
    fund = db.Column(db.Integer)
    header = db.Column(db.String(255))
    lastname = db.Column(db.String(255))
    max = db.Column(db.Integer)
    min = db.Column(db.Integer)
    opis = db.Column(db.Integer)
    opisletter = db.Column(db.String(255))
    patronymic = db.Column(db.String(255))
    periodfrom = db.Column(db.Integer)
    periodto = db.Column(db.Integer)
    registrationtype = db.Column(db.Integer)
    source_id = db.Column(db.BigInteger)
    sourcetype = db.Column(db.Integer)
    user_id = db.Column(db.BigInteger)



t_analize_source = db.Table(
    'analize_source',
    db.Column('sheet_id_min', db.BigInteger),
    db.Column('sheet_id_max', db.BigInteger),
    db.Column('source_id', db.BigInteger),
    db.Column('min', db.Integer),
    db.Column('max', db.Integer),
    db.Column('count', db.BigInteger),
    db.Column('status', db.Integer),
    db.Column('sheettype', db.Integer),
    db.Column('cnt', db.BigInteger)
)



class Applicant(db.Model):
    __tablename__ = 'applicant'

    id = db.Column(db.BigInteger, primary_key=True)
    firstname = db.Column(db.String(255))
    lastname = db.Column(db.String(255))
    mail = db.Column(db.String(255))
    patronymic = db.Column(db.String(255))
    phone = db.Column(db.String(255))



t_counting_sources = db.Table(
    'counting_sources',
    db.Column('id', db.BigInteger),
    db.Column('sourcetype', db.Integer),
    db.Column('header', db.String(255)),
    db.Column('periodfrom', db.Integer),
    db.Column('periodto', db.Integer),
    db.Column('audittalesday', db.Integer),
    db.Column('audittalesmonth', db.Integer),
    db.Column('audittalesyear', db.Integer),
    db.Column('revision', db.Integer),
    db.Column('fund', db.Integer),
    db.Column('opis', db.Integer),
    db.Column('opisletter', db.String(255)),
    db.Column('act', db.Integer),
    db.Column('actletter', db.String(255)),
    db.Column('allrecords', db.Integer),
    db.Column('opened', db.BigInteger),
    db.Column('assigment', db.BigInteger),
    db.Column('working', db.BigInteger),
    db.Column('entered', db.BigInteger),
    db.Column('approved', db.BigInteger)
)


class Bagmodel(db.Model):
    __tablename__ = 'bagmodels'

    id = db.Column(db.BigInteger, primary_key=True)
    allarchive = db.Column(db.Boolean)
    baseword = db.Column(db.String(255))
    classmodel = db.Column(db.LargeBinary)
    clustmodel = db.Column(db.LargeBinary)
    source_id = db.Column(db.ForeignKey('sourcearchive.id'))

    source = db.relationship('Sourcearchive', primaryjoin='Bagmodel.source_id == Sourcearchive.id', backref='bagmodels')

class Clustmodel(db.Model):
    __tablename__ = 'clustmodels'

    id = db.Column(db.BigInteger, primary_key=True)
    allarchive = db.Column(db.Boolean)
    model = db.Column(db.LargeBinary)
    source_id = db.Column(db.ForeignKey('sourcearchive.id'))

    source = db.relationship('Sourcearchive', primaryjoin='Clustmodel.source_id == Sourcearchive.id', backref='clustmodels')



class Documentrecord(db.Model):
    __tablename__ = 'documentrecord'

    id = db.Column(db.BigInteger, primary_key=True)
    documenttype = db.Column(db.Integer)
    content = db.Column(db.JSON)
    height = db.Column(db.Integer)
    width = db.Column(db.Integer)
    x = db.Column(db.Integer)
    y = db.Column(db.Integer)
    number = db.Column(db.Integer)
    validateresult_id = db.Column(db.ForeignKey('validateresultlist.id'))
    sheet_id = db.Column(db.ForeignKey('sheet.id'))
    listorder = db.Column(db.Integer)

    sheet = db.relationship('Sheet', primaryjoin='Documentrecord.sheet_id == Sheet.id', backref='documentrecords')
    validateresult = db.relationship('Validateresultlist', primaryjoin='Documentrecord.validateresult_id == Validateresultlist.id', backref='documentrecords')
    personss = db.relationship('Person', secondary='documentrecord_person', backref='documentrecords')



t_documentrecord_person = db.Table(
    'documentrecord_person',
    db.Column('documentrecord_entity_id', db.ForeignKey('documentrecord.id'), nullable=False),
    db.Column('persons_id', db.ForeignKey('person.id'), nullable=False, unique=True)
)



class File(db.Model):
    __tablename__ = 'files'

    id = db.Column(db.BigInteger, primary_key=True)
    name = db.Column(db.String(255), index=True)
    content = db.Column(db.LargeBinary)


class Finding(db.Model):

    __tablename__ = 'finding'

    id = db.Column(db.BigInteger, primary_key=True, server_default=db.FetchedValue())
    height = db.Column(db.Integer)
    width = db.Column(db.Integer)
    x = db.Column(db.Integer)
    y = db.Column(db.Integer)
    recognition_id = db.Column(db.ForeignKey('recognition.id'))
    sheet_id = db.Column(db.ForeignKey('sheet.id'))
    descriptorsdistance = db.Column(db.Float(53))
    hashdistance = db.Column(db.Float(53))
    hogdistance = db.Column(db.Float(53))
    modelprediction = db.Column(db.Float(53))
    tmrate = db.Column(db.Float(53))

    recognition = db.relationship('Recognition', primaryjoin='Finding.recognition_id == Recognition.id', backref='findings')
    sheet = db.relationship('Sheet', primaryjoin='Finding.sheet_id == Sheet.id', backref='findings')

    normalizedword = None

    def to_dict(self):
        finding_dict = {
            "x": self.x,
            "y": self.y,
            "h": self.height,
            "w": self.width,
            "TM_probability": int(self.tmrate*100),
            "model_prediction": int(self.modelprediction*100),
            "descriptors_distance": int(self.descriptorsdistance),
            "hash_distance": int(self.hashdistance),
            "recognition_id": self.recognition_id,
            "word_text": self.recognition.normalizedword
        }
        return finding_dict

class Firstname(db.Model):
    __tablename__ = 'firstname'

    id = db.Column(db.BigInteger, primary_key=True)
    value = db.Column(db.String(255))

    persons = db.relationship('Requestsubject', secondary='requestsubjectfirstnamemainitem', backref='firstnames')
    persons1 = db.relationship('Subject', secondary='subjectfirstnamemainitem', backref='firstnames')



class Lastname(db.Model):
    __tablename__ = 'lastname'

    id = db.Column(db.BigInteger, primary_key=True)
    value = db.Column(db.String(255))

    persons = db.relationship('Requestsubject', secondary='requestsubjectlastnamemainitem', backref='lastnames')
    persons1 = db.relationship('Subject', secondary='subjectlastnamemainitem', backref='lastnames')



class Operator(db.Model):
    __tablename__ = 'operator'

    id = db.Column(db.BigInteger, primary_key=True)
    type = db.Column(db.Integer)
    group_id = db.Column(db.ForeignKey('usergroup.id'), index=True)
    organization_id = db.Column(db.ForeignKey('organization.id'), index=True)
    user_id = db.Column(db.ForeignKey('userone.id'), index=True)

    group = db.relationship('Usergroup', primaryjoin='Operator.group_id == Usergroup.id', backref='operators')
    organization = db.relationship('Organization', primaryjoin='Operator.organization_id == Organization.id', backref='operators')
    user = db.relationship('Userone', primaryjoin='Operator.user_id == Userone.id', backref='operators')
    sheetparameters_entitys = db.relationship('Sheetparameter', secondary='sheetparameters_operator', backref='operators')



class Organization(db.Model):
    __tablename__ = 'organization'

    id = db.Column(db.BigInteger, primary_key=True)
    address = db.Column(db.String(255))
    name = db.Column(db.String(255))
    uuid = db.Column(UUID)



class Patronymic(db.Model):
    __tablename__ = 'patronymic'

    id = db.Column(db.BigInteger, primary_key=True)
    value = db.Column(db.String(255))

    persons = db.relationship('Requestsubject', secondary='requestsubjectpatronymicmainitem', backref='patronymics')
    persons1 = db.relationship('Subject', secondary='subjectlastpatronymicmainitem', backref='patronymics')



class Peopenumeration(db.Model):
    __tablename__ = 'peopenumeration'

    id = db.Column(db.BigInteger, primary_key=True)
    additional = db.Column(db.Boolean)
    code = db.Column(db.String(50))
    date = db.Column(db.String(10))
    number = db.Column(db.Integer)
    revision = db.Column(db.Integer)



class Peopenumerationhome(db.Model):
    __tablename__ = 'peopenumerationhome'

    id = db.Column(db.BigInteger, primary_key=True)
    data = db.Column(db.JSON)
    peopenumeration_id = db.Column(db.ForeignKey('peopenumeration.id'))

    peopenumeration = db.relationship('Peopenumeration', primaryjoin='Peopenumerationhome.peopenumeration_id == Peopenumeration.id', backref='peopenumerationhomes')



class Person(db.Model):
    __tablename__ = 'person'

    id = db.Column(db.BigInteger, primary_key=True)
    gender = db.Column(db.Integer)
    persontype = db.Column(db.Integer)
    firstname_id = db.Column(db.ForeignKey('firstname.id'))
    lastname_id = db.Column(db.ForeignKey('lastname.id'))
    patronymic_id = db.Column(db.ForeignKey('patronymic.id'))

    firstname = db.relationship('Firstname', primaryjoin='Person.firstname_id == Firstname.id', backref='people')
    lastname = db.relationship('Lastname', primaryjoin='Person.lastname_id == Lastname.id', backref='people')
    patronymic = db.relationship('Patronymic', primaryjoin='Person.patronymic_id == Patronymic.id', backref='people')



class Personfirstnamealteritem(db.Model):
    __tablename__ = 'personfirstnamealteritem'

    person_id = db.Column(db.ForeignKey('person.id'), primary_key=True, nullable=False, index=True)
    item_id = db.Column(db.ForeignKey('firstname.id'), nullable=False, unique=True)
    listindex = db.Column(db.Integer, primary_key=True, nullable=False)

    item = db.relationship('Firstname', uselist=False, primaryjoin='Personfirstnamealteritem.item_id == Firstname.id', backref='personfirstnamealteritems')
    person = db.relationship('Person', primaryjoin='Personfirstnamealteritem.person_id == Person.id', backref='personfirstnamealteritems')



class Personlastnamealteritem(db.Model):
    __tablename__ = 'personlastnamealteritem'

    person_id = db.Column(db.ForeignKey('person.id'), primary_key=True, nullable=False, index=True)
    item_id = db.Column(db.ForeignKey('lastname.id'), nullable=False, unique=True)
    listindex = db.Column(db.Integer, primary_key=True, nullable=False)

    item = db.relationship('Lastname', uselist=False, primaryjoin='Personlastnamealteritem.item_id == Lastname.id', backref='personlastnamealteritems')
    person = db.relationship('Person', primaryjoin='Personlastnamealteritem.person_id == Person.id', backref='personlastnamealteritems')



class Personpatronymicalteritem(db.Model):
    __tablename__ = 'personpatronymicalteritem'

    person_id = db.Column(db.ForeignKey('person.id'), primary_key=True, nullable=False, index=True)
    item_id = db.Column(db.ForeignKey('patronymic.id'), nullable=False, unique=True)
    listindex = db.Column(db.Integer, primary_key=True, nullable=False)

    item = db.relationship('Patronymic', uselist=False, primaryjoin='Personpatronymicalteritem.item_id == Patronymic.id', backref='personpatronymicalteritems')
    person = db.relationship('Person', primaryjoin='Personpatronymicalteritem.person_id == Person.id', backref='personpatronymicalteritems')



class Property(db.Model):
    __tablename__ = 'property'

    id = db.Column(db.BigInteger, primary_key=True)
    propertykey = db.Column(db.String(255), unique=True)
    propertyvalue = db.Column(db.String(1023), index=True)



class Recognition(db.Model):
    __tablename__ = 'recognition'

    id = db.Column(db.BigInteger, primary_key=True)
    findingword = db.Column(db.String(255))
    height = db.Column(db.Integer)
    width = db.Column(db.Integer)
    x = db.Column(db.Integer)
    y = db.Column(db.Integer)
    number = db.Column(db.Integer, index=True)
    recognitiontype = db.Column(db.Integer)
    normalizedword = db.Column(db.String(255), index=True)
    scanfragment_id = db.Column(db.ForeignKey('scancontent.id'))
    threshold = db.Column(db.Float)
    perchash = db.Column(db.String(1000))

    scanfragment = db.relationship('Scancontent', primaryjoin='Recognition.scanfragment_id == Scancontent.id', backref='recognitions')
    sheet_entitys = db.relationship('Sheet', secondary='sheet_recognition', backref='recognitions')

t_recognition_image_sizes = db.Table(
    'recognition_image_sizes',
    db.Column('id', db.BigInteger),
    db.Column('imagewidth', db.Integer),
    db.Column('imageheight', db.Integer)
)

class Recognitionbybasename(db.Model):
    __tablename__ = 'recognitionbybasename'

    id = db.Column(db.BigInteger, primary_key=True, server_default=db.FetchedValue())
    basename = db.Column(db.String(255))
    recognition_id = db.Column(db.ForeignKey('recognition.id'))

    recognition = db.relationship('Recognition', primaryjoin='Recognitionbybasename.recognition_id == Recognition.id', backref='recognitionbybasenames')

class Relation(db.Model):
    __tablename__ = 'relations'

    id = db.Column(db.BigInteger, primary_key=True)
    agefromreceiver = db.Column(db.Integer)
    agefromsource = db.Column(db.Integer)
    agetoreceiver = db.Column(db.Integer)
    agetosource = db.Column(db.Integer)
    datefromday = db.Column(db.Integer)
    datefrommonth = db.Column(db.Integer)
    datefromyeay = db.Column(db.Integer)
    datetoday = db.Column(db.Integer)
    datetomonth = db.Column(db.Integer)
    datetoyeay = db.Column(db.Integer)
    indexnumber = db.Column(db.Integer)
    type = db.Column(db.Integer)
    uuid = db.Column(UUID)
    address_id = db.Column(db.ForeignKey('address.id'))
    receiver_id = db.Column(db.ForeignKey('subject.id'))
    source_id = db.Column(db.ForeignKey('subject.id'))

    address = db.relationship('Addres', primaryjoin='Relation.address_id == Addres.id', backref='relations')
    receiver = db.relationship('Subject', primaryjoin='Relation.receiver_id == Subject.id', backref='subject_relations')
    source = db.relationship('Subject', primaryjoin='Relation.source_id == Subject.id', backref='subject_relations_0')
    request_entitys = db.relationship('Request', secondary='request_relations', backref='relations')



class Request(db.Model):
    __tablename__ = 'request'

    id = db.Column(db.BigInteger, primary_key=True)
    date = db.Column(db.Date)
    note = db.Column(db.String(255))
    number = db.Column(db.Integer)
    status = db.Column(db.Integer)
    applicant_id = db.Column(db.ForeignKey('applicant.id'))
    requestsubject_id = db.Column(db.ForeignKey('requestsubject.id'))

    applicant = db.relationship('Applicant', primaryjoin='Request.applicant_id == Applicant.id', backref='requests')
    requestsubject = db.relationship('Requestsubject', primaryjoin='Request.requestsubject_id == Requestsubject.id', backref='requests')



t_request_relations = db.Table(
    'request_relations',
    db.Column('request_entity_id', db.ForeignKey('request.id'), nullable=False),
    db.Column('relations_id', db.ForeignKey('relations.id'), nullable=False, unique=True)
)



class RequestSubject(db.Model):
    __tablename__ = 'request_subject'

    request_entity_id = db.Column(db.ForeignKey('request.id'), primary_key=True, nullable=False)
    subjects_id = db.Column(db.ForeignKey('subject.id'), nullable=False, unique=True)
    order_column = db.Column(db.Integer, primary_key=True, nullable=False)

    request_entity = db.relationship('Request', primaryjoin='RequestSubject.request_entity_id == Request.id', backref='request_subjects')
    subjects = db.relationship('Subject', uselist=False, primaryjoin='RequestSubject.subjects_id == Subject.id', backref='request_subjects')



class Requestmarriage(db.Model):
    __tablename__ = 'requestmarriage'

    id = db.Column(db.BigInteger, primary_key=True)
    agefromhusband = db.Column(db.Integer)
    agefromwife = db.Column(db.Integer)
    agetohusband = db.Column(db.Integer)
    agetowife = db.Column(db.Integer)
    childcount = db.Column(db.Integer)
    datefromday = db.Column(db.Integer)
    datefrommonth = db.Column(db.Integer)
    datefromyeay = db.Column(db.Integer)
    datetoday = db.Column(db.Integer)
    datetomonth = db.Column(db.Integer)
    datetoyeay = db.Column(db.Integer)
    uuid = db.Column(UUID)
    address_id = db.Column(db.ForeignKey('address.id'))

    address = db.relationship('Addres', primaryjoin='Requestmarriage.address_id == Addres.id', backref='requestmarriages')
    requestsubject_entitys = db.relationship('Requestsubject', secondary='requestsubject_requestmarriage', backref='requestmarriages')



class Requestsubject(db.Model):
    __tablename__ = 'requestsubject'

    id = db.Column(db.BigInteger, primary_key=True)
    birthfromday = db.Column(db.Integer)
    birthfrommonth = db.Column(db.Integer)
    birthfromyeay = db.Column(db.Integer)
    birthtoday = db.Column(db.Integer)
    birthtomonth = db.Column(db.Integer)
    birthtoyeay = db.Column(db.Integer)
    deathagefrom = db.Column(db.Integer)
    deathageto = db.Column(db.Integer)
    deathfromday = db.Column(db.Integer)
    deathfrommonth = db.Column(db.Integer)
    deathfromyeay = db.Column(db.Integer)
    deathtoday = db.Column(db.Integer)
    deathtomonth = db.Column(db.Integer)
    deathtoyeay = db.Column(db.Integer)
    gender = db.Column(db.Integer)
    marriagecount = db.Column(db.Integer)
    birthaddress_id = db.Column(db.ForeignKey('address.id'))
    deathaddress_id = db.Column(db.ForeignKey('address.id'))

    birthaddress = db.relationship('Addres', primaryjoin='Requestsubject.birthaddress_id == Addres.id', backref='addres_requestsubjects')
    deathaddress = db.relationship('Addres', primaryjoin='Requestsubject.deathaddress_id == Addres.id', backref='addres_requestsubjects_0')



t_requestsubject_requestmarriage = db.Table(
    'requestsubject_requestmarriage',
    db.Column('requestsubject_entity_id', db.ForeignKey('requestsubject.id'), nullable=False),
    db.Column('marriage_id', db.ForeignKey('requestmarriage.id'), nullable=False, unique=True)
)



class Requestsubjectfirstnamealteritem(db.Model):
    __tablename__ = 'requestsubjectfirstnamealteritem'

    person_id = db.Column(db.ForeignKey('requestsubject.id'), primary_key=True, nullable=False, index=True)
    item_id = db.Column(db.ForeignKey('firstname.id'), nullable=False, unique=True)
    listindex = db.Column(db.Integer, primary_key=True, nullable=False)

    item = db.relationship('Firstname', uselist=False, primaryjoin='Requestsubjectfirstnamealteritem.item_id == Firstname.id', backref='requestsubjectfirstnamealteritems')
    person = db.relationship('Requestsubject', primaryjoin='Requestsubjectfirstnamealteritem.person_id == Requestsubject.id', backref='requestsubjectfirstnamealteritems')



t_requestsubjectfirstnamemainitem = db.Table(
    'requestsubjectfirstnamemainitem',
    db.Column('item_id', db.ForeignKey('firstname.id')),
    db.Column('person_id', db.ForeignKey('requestsubject.id'), primary_key=True)
)



class Requestsubjectlastnamealteritem(db.Model):
    __tablename__ = 'requestsubjectlastnamealteritem'

    person_id = db.Column(db.ForeignKey('requestsubject.id'), primary_key=True, nullable=False, index=True)
    item_id = db.Column(db.ForeignKey('lastname.id'), nullable=False, unique=True)
    listindex = db.Column(db.Integer, primary_key=True, nullable=False)

    item = db.relationship('Lastname', uselist=False, primaryjoin='Requestsubjectlastnamealteritem.item_id == Lastname.id', backref='requestsubjectlastnamealteritems')
    person = db.relationship('Requestsubject', primaryjoin='Requestsubjectlastnamealteritem.person_id == Requestsubject.id', backref='requestsubjectlastnamealteritems')



t_requestsubjectlastnamemainitem = db.Table(
    'requestsubjectlastnamemainitem',
    db.Column('item_id', db.ForeignKey('lastname.id')),
    db.Column('person_id', db.ForeignKey('requestsubject.id'), primary_key=True)
)



class Requestsubjectpatronymicalteritem(db.Model):
    __tablename__ = 'requestsubjectpatronymicalteritem'

    person_id = db.Column(db.ForeignKey('requestsubject.id'), primary_key=True, nullable=False, index=True)
    item_id = db.Column(db.ForeignKey('patronymic.id'), nullable=False, unique=True)
    listindex = db.Column(db.Integer, primary_key=True, nullable=False)

    item = db.relationship('Patronymic', uselist=False, primaryjoin='Requestsubjectpatronymicalteritem.item_id == Patronymic.id', backref='requestsubjectpatronymicalteritems')
    person = db.relationship('Requestsubject', primaryjoin='Requestsubjectpatronymicalteritem.person_id == Requestsubject.id', backref='requestsubjectpatronymicalteritems')



t_requestsubjectpatronymicmainitem = db.Table(
    'requestsubjectpatronymicmainitem',
    db.Column('item_id', db.ForeignKey('patronymic.id')),
    db.Column('person_id', db.ForeignKey('requestsubject.id'), primary_key=True)
)



class Role(db.Model):
    __tablename__ = 'role'

    id = db.Column(db.BigInteger, primary_key=True)
    name = db.Column(db.String(255))

    usersecureds = db.relationship('Usersecured', secondary='usersecuredroles', backref='roles')



t_roleprivileges = db.Table(
    'roleprivileges',
    db.Column('role_id', db.ForeignKey('role.id'), nullable=False),
    db.Column('privileges', db.String(255))
)



class Scancontent(db.Model):
    __tablename__ = 'scancontent'

    id = db.Column(db.BigInteger, primary_key=True)
    content = db.Column(db.LargeBinary)



class Searchrecord(db.Model):
    __tablename__ = 'searchrecord'

    id = db.Column(db.BigInteger, primary_key=True)
    church = db.Column(db.String(255))
    type = db.Column(db.Integer)
    yearfrom = db.Column(db.Integer)
    yearto = db.Column(db.Integer)
    child_id = db.Column(db.ForeignKey('subject.id'))
    parishaddress_id = db.Column(db.ForeignKey('address.id'))
    record_id = db.Column(db.ForeignKey('documentrecord.id'))
    relations_id = db.Column(db.ForeignKey('relations.id'))
    sheet_id = db.Column(db.ForeignKey('sheet.id'))

    child = db.relationship('Subject', primaryjoin='Searchrecord.child_id == Subject.id', backref='subject_subject_searchrecords')
    parishaddress = db.relationship('Addres', primaryjoin='Searchrecord.parishaddress_id == Addres.id', backref='searchrecords')
    record = db.relationship('Documentrecord', primaryjoin='Searchrecord.record_id == Documentrecord.id', backref='searchrecords')
    relations = db.relationship('Relation', primaryjoin='Searchrecord.relations_id == Relation.id', backref='searchrecords')
    sheet = db.relationship('Sheet', primaryjoin='Searchrecord.sheet_id == Sheet.id', backref='searchrecords')
    sourcess = db.relationship('Sourcearchive', secondary='searchrecord_sourcearchive', backref='searchrecords')
    subjects = db.relationship('Subject', secondary='subject_sourcesbirthchild', backref='subject_subject_searchrecords_0')



t_searchrecord_sourcearchive = db.Table(
    'searchrecord_sourcearchive',
    db.Column('searchrecord_entity_id', db.ForeignKey('searchrecord.id'), nullable=False),
    db.Column('sources_id', db.ForeignKey('sourcearchive.id'), nullable=False)
)



class Sheet(db.Model):
    __tablename__ = 'sheet'

    id = db.Column(db.BigInteger, primary_key=True)
    approveddate = db.Column(db.DateTime)
    comment = db.Column(db.String(512))
    date = db.Column(db.DateTime)
    dateuntil = db.Column(db.DateTime)
    entereddate = db.Column(db.DateTime)
    filename = db.Column(db.String(255))
    number = db.Column(db.Integer)
    numberback = db.Column(db.Integer)
    numberface = db.Column(db.Integer)
    onlyone = db.Column(db.Boolean)
    registrationtype = db.Column(db.Integer)
    scanfilepath = db.Column(db.String(255))
    sheettype = db.Column(db.Integer)
    status = db.Column(db.Integer)
    sourcetype = db.Column(db.Integer)
    content = db.Column(db.JSON)
    approveduser_id = db.Column(db.ForeignKey('userone.id'))
    parameters_id = db.Column(db.ForeignKey('sheetparameters.id'))
    source_id = db.Column(db.ForeignKey('sourcearchive.id'))
    user_id = db.Column(db.ForeignKey('userone.id'))
    imageheight = db.Column(db.Integer)
    imagewidth = db.Column(db.Integer)

    approveduser = db.relationship('Userone', primaryjoin='Sheet.approveduser_id == Userone.id', backref='userone_sheets')
    parameters = db.relationship('Sheetparameter', primaryjoin='Sheet.parameters_id == Sheetparameter.id', backref='sheets')
    source = db.relationship('Sourcearchive', primaryjoin='Sheet.source_id == Sourcearchive.id', backref='sheets')
    user = db.relationship('Userone', primaryjoin='Sheet.user_id == Userone.id', backref='userone_sheets_0')




t_sheet_recognition = db.Table(
    'sheet_recognition',
    db.Column('sheet_entity_id', db.ForeignKey('sheet.id'), nullable=False),
    db.Column('recognition_id', db.ForeignKey('recognition.id'), nullable=False, unique=True)
)



class Sheetparameter(db.Model):
    __tablename__ = 'sheetparameters'

    id = db.Column(db.BigInteger, primary_key=True)
    allusers = db.Column(db.Boolean, index=True)
    audittalescontractnumbercurrentrevision = db.Column(db.Boolean)
    audittalescontractnumberprevrevision = db.Column(db.Boolean)
    audittaleslastname = db.Column(db.Boolean)
    date = db.Column(db.DateTime)
    owner = db.Column(db.Boolean)
    parish = db.Column(db.Boolean)
    priest = db.Column(db.Boolean)
    recipients = db.Column(db.Boolean)
    status = db.Column(db.Integer)
    surety = db.Column(db.Boolean)



t_sheetparameters_operator = db.Table(
    'sheetparameters_operator',
    db.Column('sheetparameters_entity_id', db.ForeignKey('sheetparameters.id'), nullable=False),
    db.Column('operators_id', db.ForeignKey('operator.id'), nullable=False, unique=True)
)



class Sheetstatushistory(db.Model):
    __tablename__ = 'sheetstatushistory'

    id = db.Column(db.BigInteger, primary_key=True)
    date = db.Column(db.DateTime)
    dateuntil = db.Column(db.DateTime)
    status = db.Column(db.Integer)
    author_id = db.Column(db.ForeignKey('userone.id'))
    user_id = db.Column(db.ForeignKey('userone.id'))
    sheet_id = db.Column(db.ForeignKey('sheet.id'))
    listorder = db.Column(db.Integer)

    author = db.relationship('Userone', primaryjoin='Sheetstatushistory.author_id == Userone.id', backref='userone_sheetstatushistories')
    sheet = db.relationship('Sheet', primaryjoin='Sheetstatushistory.sheet_id == Sheet.id', backref='sheetstatushistories')
    user = db.relationship('Userone', primaryjoin='Sheetstatushistory.user_id == Userone.id', backref='userone_sheetstatushistories_0')



t_source_content = db.Table(
    'source_content',
    db.Column('minimum', db.Integer),
    db.Column('maximum', db.Integer),
    db.Column('allsheet', db.Integer),
    db.Column('entered', db.BigInteger),
    db.Column('approved', db.BigInteger),
    db.Column('parameters_id', db.BigInteger),
    db.Column('operators_name', db.Text),
    db.Column('status', db.Integer),
    db.Column('source_id', db.BigInteger),
    db.Column('group_nr', db.BigInteger),
    db.Column('date', db.DateTime)
)



class Sourcearchive(db.Model):
    __tablename__ = 'sourcearchive'

    id = db.Column(db.BigInteger, primary_key=True)
    allrecords = db.Column(db.Integer)
    audittalesday = db.Column(db.Integer)
    audittalesmonth = db.Column(db.Integer)
    audittalesyear = db.Column(db.Integer)
    act = db.Column(db.Integer)
    actletter = db.Column(db.String(255))
    fund = db.Column(db.Integer)
    opis = db.Column(db.Integer)
    opisletter = db.Column(db.String(255))
    header = db.Column(db.String(255))
    periodfrom = db.Column(db.Integer, index=True)
    periodto = db.Column(db.Integer, index=True)
    revision = db.Column(db.Integer)
    sourcetype = db.Column(db.Integer, index=True)



class Subject(db.Model):
    __tablename__ = 'subject'

    id = db.Column(db.BigInteger, primary_key=True)
    abstractable = db.Column(db.Boolean)
    birthfromday = db.Column(db.Integer)
    birthfrommonth = db.Column(db.Integer)
    birthfromyeay = db.Column(db.Integer)
    birthtoday = db.Column(db.Integer)
    birthtomonth = db.Column(db.Integer)
    birthtoyeay = db.Column(db.Integer)
    deathagefrom = db.Column(db.Integer)
    deathageto = db.Column(db.Integer)
    deathfromday = db.Column(db.Integer)
    deathfrommonth = db.Column(db.Integer)
    deathfromyeay = db.Column(db.Integer)
    deathtoday = db.Column(db.Integer)
    deathtomonth = db.Column(db.Integer)
    deathtoyeay = db.Column(db.Integer)
    gender = db.Column(db.Integer)
    uuid = db.Column(UUID, index=True)
    birthaddress_id = db.Column(db.ForeignKey('address.id'))
    deathaddress_id = db.Column(db.ForeignKey('address.id'))
    sourcesaudittales_id = db.Column(db.ForeignKey('searchrecord.id'))
    sourcesbirth_id = db.Column(db.ForeignKey('searchrecord.id'))
    sourcesdeath_id = db.Column(db.ForeignKey('searchrecord.id'))

    birthaddress = db.relationship('Addres', primaryjoin='Subject.birthaddress_id == Addres.id', backref='addres_subjects')
    deathaddress = db.relationship('Addres', primaryjoin='Subject.deathaddress_id == Addres.id', backref='addres_subjects_0')
    sourcesaudittales = db.relationship('Searchrecord', primaryjoin='Subject.sourcesaudittales_id == Searchrecord.id', backref='searchrecord_searchrecord_subjects')
    sourcesbirth = db.relationship('Searchrecord', primaryjoin='Subject.sourcesbirth_id == Searchrecord.id', backref='searchrecord_searchrecord_subjects_0')



t_subject_sourcesbirthchild = db.Table(
    'subject_sourcesbirthchild',
    db.Column('subject_id', db.ForeignKey('subject.id'), nullable=False, index=True),
    db.Column('source_record_id', db.ForeignKey('searchrecord.id'), nullable=False, index=True)
)



t_subject_sourcesmarriage = db.Table(
    'subject_sourcesmarriage',
    db.Column('subject_id', db.ForeignKey('subject.id'), nullable=False, index=True),
    db.Column('source_record_id', db.ForeignKey('searchrecord.id'), nullable=False, index=True)
)



class Subjectfirstnamealteritem(db.Model):
    __tablename__ = 'subjectfirstnamealteritem'

    person_id = db.Column(db.ForeignKey('subject.id'), primary_key=True, nullable=False, index=True)
    item_id = db.Column(db.ForeignKey('firstname.id'), nullable=False, unique=True)
    listindex = db.Column(db.Integer, primary_key=True, nullable=False)

    item = db.relationship('Firstname', uselist=False, primaryjoin='Subjectfirstnamealteritem.item_id == Firstname.id', backref='subjectfirstnamealteritems')
    person = db.relationship('Subject', primaryjoin='Subjectfirstnamealteritem.person_id == Subject.id', backref='subjectfirstnamealteritems')



t_subjectfirstnamemainitem = db.Table(
    'subjectfirstnamemainitem',
    db.Column('item_id', db.ForeignKey('firstname.id')),
    db.Column('person_id', db.ForeignKey('subject.id'), primary_key=True)
)



class Subjectlastnamealteritem(db.Model):
    __tablename__ = 'subjectlastnamealteritem'

    person_id = db.Column(db.ForeignKey('subject.id'), primary_key=True, nullable=False, index=True)
    item_id = db.Column(db.ForeignKey('lastname.id'), nullable=False, unique=True)
    listindex = db.Column(db.Integer, primary_key=True, nullable=False)

    item = db.relationship('Lastname', uselist=False, primaryjoin='Subjectlastnamealteritem.item_id == Lastname.id', backref='subjectlastnamealteritems')
    person = db.relationship('Subject', primaryjoin='Subjectlastnamealteritem.person_id == Subject.id', backref='subjectlastnamealteritems')



t_subjectlastnamemainitem = db.Table(
    'subjectlastnamemainitem',
    db.Column('item_id', db.ForeignKey('lastname.id')),
    db.Column('person_id', db.ForeignKey('subject.id'), primary_key=True)
)



class Subjectlastpatronymicalteritem(db.Model):
    __tablename__ = 'subjectlastpatronymicalteritem'

    person_id = db.Column(db.ForeignKey('subject.id'), primary_key=True, nullable=False, index=True)
    item_id = db.Column(db.ForeignKey('patronymic.id'), nullable=False, unique=True)
    listindex = db.Column(db.Integer, primary_key=True, nullable=False)

    item = db.relationship('Patronymic', uselist=False, primaryjoin='Subjectlastpatronymicalteritem.item_id == Patronymic.id', backref='subjectlastpatronymicalteritems')
    person = db.relationship('Subject', primaryjoin='Subjectlastpatronymicalteritem.person_id == Subject.id', backref='subjectlastpatronymicalteritems')



t_subjectlastpatronymicmainitem = db.Table(
    'subjectlastpatronymicmainitem',
    db.Column('item_id', db.ForeignKey('patronymic.id')),
    db.Column('person_id', db.ForeignKey('subject.id'), primary_key=True)
)



t_user_sheets_by_status = db.Table(
    'user_sheets_by_status',
    db.Column('sheet_id_min', db.BigInteger),
    db.Column('sheet_id_max', db.BigInteger),
    db.Column('source_id', db.BigInteger),
    db.Column('sourcetype', db.Integer),
    db.Column('header', db.String(255)),
    db.Column('fund', db.Integer),
    db.Column('opis', db.Integer),
    db.Column('opisletter', db.String(255)),
    db.Column('act', db.Integer),
    db.Column('actletter', db.String(255)),
    db.Column('periodfrom', db.Integer),
    db.Column('periodto', db.Integer),
    db.Column('audittalesday', db.Integer),
    db.Column('audittalesmonth', db.Integer),
    db.Column('audittalesyear', db.Integer),
    db.Column('revision', db.Integer),
    db.Column('min', db.Integer),
    db.Column('max', db.Integer),
    db.Column('count', db.BigInteger),
    db.Column('status', db.Integer),
    db.Column('user_id', db.BigInteger),
    db.Column('allusers', db.Boolean)
)



class Usergroup(db.Model):
    __tablename__ = 'usergroup'

    id = db.Column(db.BigInteger, primary_key=True)
    name = db.Column(db.String(255))



t_usergroup_userone = db.Table(
    'usergroup_userone',
    db.Column('usergroup_entity_id', db.ForeignKey('usergroup.id'), nullable=False),
    db.Column('user_id', db.ForeignKey('userone.id'), nullable=False)
)



class Userlived(db.Model):
    __tablename__ = 'userlived'

    id = db.Column(db.BigInteger, primary_key=True)
    userone_id = db.Column(db.ForeignKey('userone.id'))

    userone = db.relationship('Userone', primaryjoin='Userlived.userone_id == Userone.id', backref='userliveds')



class Userone(db.Model):
    __tablename__ = 'userone'

    id = db.Column(db.BigInteger, primary_key=True)
    firstname = db.Column(db.String(255))
    lastname = db.Column(db.String(255))
    patronymic = db.Column(db.String(255))
    phone = db.Column(db.String(255))
    post = db.Column(db.String(255))
    organization_id = db.Column(db.ForeignKey('organization.id'))

    organization = db.relationship('Organization', primaryjoin='Userone.organization_id == Organization.id', backref='userones')
    usergroup_entitys = db.relationship('Usergroup', secondary='usergroup_userone', backref='userones')



class Useropened(db.Model):
    __tablename__ = 'useropened'

    id = db.Column(db.BigInteger, primary_key=True)
    blocked = db.Column(db.Boolean)
    fromsecured = db.Column(db.Boolean)
    login = db.Column(db.String(255), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)
    lived_id = db.Column(db.ForeignKey('userlived.id'))

    lived = db.relationship('Userlived', primaryjoin='Useropened.lived_id == Userlived.id', backref='useropeneds')



class Usersecured(db.Model):
    __tablename__ = 'usersecured'

    id = db.Column(db.BigInteger, primary_key=True)
    login = db.Column(db.String(255))
    password = db.Column(db.String(255))
    lived_id = db.Column(db.ForeignKey('userlived.id'))

    lived = db.relationship('Userlived', primaryjoin='Usersecured.lived_id == Userlived.id', backref='usersecureds')



t_usersecuredroles = db.Table(
    'usersecuredroles',
    db.Column('usersecured_id', db.ForeignKey('usersecured.id'), nullable=False, index=True),
    db.Column('role_id', db.ForeignKey('role.id'), nullable=False, index=True)
)



class Validateresult(db.Model):
    __tablename__ = 'validateresult'

    id = db.Column(db.BigInteger, primary_key=True)
    message = db.Column(db.String(255))
    type = db.Column(db.Integer)
    list_id = db.Column(db.ForeignKey('validateresultlist.id'))

    list = db.relationship('Validateresultlist', primaryjoin='Validateresult.list_id == Validateresultlist.id', backref='validateresults')



class Validateresultlist(db.Model):
    __tablename__ = 'validateresultlist'

    id = db.Column(db.BigInteger, primary_key=True)
    count = db.Column(db.Integer)
    type = db.Column(db.Integer)
