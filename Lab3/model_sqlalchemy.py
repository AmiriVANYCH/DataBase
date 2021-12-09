from sqlalchemy import create_engine, Column, SmallInteger, BigInteger, String, Date, select
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import *
from sqlalchemy.orm import relationship, backref, sessionmaker, Session
from sqlalchemy.orm import *
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy import inspect
from sqlalchemy.sql.expression import func
#from sqlalchemy import func, and_, or_, not
from datetime import date

Base = declarative_base()

# Клас, що описує таблицю CarType


class CarType(Base):
    __tablename__ = 'CarType'
    CarTypeID = Column('CarTypeID', SmallInteger, primary_key=True)
    CarTypeName = Column('CarTypeName', String(255), nullable=False)
    cars = relationship("Cars", back_populates="cartype")

    # Ця частина коду використовується, коли ми повертаємо
    # інформацію у контролер. Контролер очірує дані у форматі
    # python Dictionary

    def to_dict(self):
        dict = {}
        dict["CarTypeID"] = self.CarTypeID
        dict["CarTypeName"] = self.CarTypeName
        return dict


# Клас, що описує таблицю Makes


class Makes(Base):
    __tablename__ = 'Makes'
    MakeID = Column('MakeID', SmallInteger, primary_key=True)
    MakeName = Column('MakeName', String(50), nullable=False)
    MakeDescription = Column('MakeDescription', String)
    cars = relationship("Cars", back_populates="makes")

    def to_dict(self):
        dict = {}
        dict["MakeID"] = self.MakeID
        dict["MakeName"] = self.MakeName
        dict["MakeDescription"] = self.MakeDescription
        return dict


# Клас, що описує таблицю Cars


class Cars(Base):
    __tablename__ = 'Cars'
    CarRegNum = Column('CarRegNum', String(8), primary_key=True)
    CarMakeID = Column(ForeignKey('Makes.MakeID'), primary_key=True)
    CarType = Column('CarType', SmallInteger, ForeignKey('CarType.CarTypeID'))
    cartype = relationship("CarType", back_populates="cars")
    makes = relationship("Makes", back_populates="cars")
    person = relationship(
        "Contract", cascade="all, delete, delete-orphan", back_populates="cars")

    def to_dict(self):
        dict = {}
        dict["CarRegNum"] = self.CarRegNum
        dict["CarMakeID"] = self.CarMakeID
        dict["CarType"] = self.CarType
        return dict

# Клас, що описує таблицю ParkingPlace


class ParkingPlace(Base):
    __tablename__ = 'ParkingPlace'
    ParkingPlaceID = Column('ParkingPlaceID', SmallInteger, primary_key=True)
    ParkingPlaceDesc = Column('ParkingPlaceDesc', String)
    contract = relationship("Contract", back_populates="parking")

    def to_dict(self):
        dict = {}
        dict["ParkingPlaceID"] = self.ParkingPlaceID
        dict["ParkingPlaceDesc"] = self.ParkingPlaceDesc
        return dict

# Клас, що описує таблицю Persons


class Persons(Base):
    __tablename__ = 'Persons'
    PersonID = Column('PersonID', BigInteger, primary_key=True)
    PersonLastName = Column('PersonLastName', String(50), nullable=False)
    PersonName = Column('PersonName', String(50), nullable=False)
    PersonMidleName = Column('PersonMidleName', String(50))
    cars = relationship(
        "Contract", cascade="all, delete, delete-orphan", back_populates="person")
    phones = relationship(
        "Phones", cascade="all, delete, delete-orphan", back_populates="person")

    def to_dict(self):
        dict = {}
        dict["PersonID"] = self.PersonID
        dict["PersonLastName"] = self.PersonLastName
        dict["PersonName"] = self.PersonName
        dict["PersonMidleName"] = self.PersonMidleName
        return dict

# Клас, що описує таблицю Phones


class Phones(Base):
    __tablename__ = 'Phones'
    Phone = Column('Phone', BigInteger, primary_key=True)
    PersonID = Column(ForeignKey('Persons.PersonID'), primary_key=True)
    person = relationship("Persons", back_populates="phones")

    def to_dict(self):
        dict = {}
        dict["Phone"] = self.Phone
        dict["PersonID"] = self.PersonID
        return dict

# Клас, що описує таблицю Contract, у той самий час є асоціативним
# класом, що утворює звязок N:M багато до багатьох між сутностями
# Persons та Cars


class Contract(Base):
    __tablename__ = 'Contract'
    ContractID = Column('ContractID', BigInteger, primary_key=True)
    CarNumber = Column(ForeignKey('Cars.CarRegNum'), primary_key=True)
    PersonID = Column(ForeignKey('Persons.PersonID'), primary_key=True)
    ParkingID = Column(ForeignKey(
        'ParkingPlace.ParkingPlaceID'), primary_key=True)
    ContractStart = Column('ContractStart', Date, nullable=False)
    ContractEnd = Column('ContractEnd', Date, nullable=False)
    cars = relationship("Cars", back_populates="person")
    person = relationship("Persons", back_populates="cars")
    parking = relationship("ParkingPlace", back_populates="contract")

    def to_dict(self):
        dict = {}
        dict["ContractID"] = self.ContractID
        dict["CarNumber"] = self.CarNumber
        dict["PersonID"] = self.PersonID
        dict["ParkingID"] = self.ParkingID
        dict["ContractStart"] = self.ContractStart
        dict["ContractEnd"] = self.ContractEnd
        return dict


class ModelBasic(object):

    _connection = None
    _cursor = None
    _engine = None
    _session = None

    def list2dict(self, list):
        dict = []
        for row in list:
            dict.append(row.to_dict())
        return dict

    def sqlaRecord2dict(self, record):
        dict = {}
        for r in record:
            dict.update(r.to_dict())
        return dict

    def sqlaListRecordsToDict(self, record):
        dict = {}
        if record is not None:
            for row in record:
                d = self.sqlaRecord2dict(row)
                dict.append(d)
        return dict

    def get_connection(self):

        if not self._engine:
            self._engine = create_engine(
                'postgresql://ivan:12345678@192.168.1.224:5432/Parking')
        return self._engine

    def get_cursor(self):
        if self._session:
            return self._session
        else:
            engine = self.get_connection()
            Session = sessionmaker(bind=engine)
            self._session = Session()
            return self._session

    def get_make_by_name(self, makeName):
        record = self._get_make_by_name(makeName)
        return record.to_dict()

    def _get_make_by_name(self, makeName):
        session = self.get_cursor()
        record = session.query(Makes).filter_by(MakeName=makeName).first()
        return record

    def _get_make_by_id(self, makeID):
        session = self.get_cursor()
        record = session.query(Makes).filter_by(MakeID=makeID).first()
        return record

    def get_make_by_id(self, makeID):
        record = self._get_make_by_id(makeID)
        return record.to_dict()

    def create_make(self, makeName, MakeDescription=''):
        session = self.get_cursor()
        record = self._get_make_by_name(makeName)
        if not hasattr(record, 'MakeID'):
            make = Makes(
                MakeName=makeName,
                MakeDescription=MakeDescription)
            session.add(make)
            session.commit()

    def read_make(self):
        session = self.get_cursor()
        record = session.query(Makes).all()
        return self.list2dict(record)

    def update_make(self, MakeID, MakeName, MakeDescription=''):
        session = self.get_cursor()
        record = self._get_make_by_id(MakeID)
        if hasattr(record, 'MakeID'):
            record.MakeName = MakeName
            record.MakeDescription = MakeDescription
            session.commit()

    def del_make(self, MakeID):
        session = self.get_cursor()
        Makes.query.filter(Makes.MakeID == MakeID).delete()
        session.commit()

##############Type

    def _get_CarType_by_name(self, CarTypeName):
        session = self.get_cursor()
        record = session.query(CarType).filter_by(
            CarTypeName=CarTypeName).first()
        return record

    def get_CarType_by_name(self, CarTypeName):
        return self._get_CarType_by_name(CarTypeName).to_dict()

    def _get_CarType_by_id(self, CarTypeID):
        session = self.get_cursor()
        record = session.query(CarType).filter_by(
            CarTypeID=CarTypeID).first()
        return record

    def get_CarType_by_id(self, CarTypeID):
        return self._get_CarType_by_id(CarTypeID).to_dict()

    def create_CarType(self, CarTypeName):
        session = self.get_cursor()
        record = self._get_CarType_by_name(CarTypeName)
        if not hasattr(record, 'CarTypeID'):
            cartype = CarType(
                CarTypeName=CarTypeName)
            session.add(cartype)
            session.commit()

    def read_CarType(self,):
        session = self.get_cursor()
        record = session.query(CarType).all()
        return self.list2dict(record)

    def update_CarType(self, CarTypeID, CarTypeName):
        session = self.get_cursor()
        record = self._get_CarType_by_id(CarTypeID)
        if hasattr(record, 'CarTypeID'):
            record.CarTypeName = CarTypeName
            session.commit()

    def del_CarType(self, CarTypeID):
        session = self.get_cursor()
        CarType.query.filter(CarType.CarTypeID == CarTypeID).delete()
        session.commit()

    ########Cars

    def _get_Car_by_Reg_num(self, CarRegNum):
        session = self.get_cursor()
        record = session.query(Cars).filter_by(
            CarRegNum=CarRegNum).first()
        return record

    def get_Car_by_Reg_num(self, CarRegNum):
        return self._get_Car_by_Reg_num(CarRegNum).to_dict()

    def create_Car(self, CarRegNum, CarMakeID, CarType):
        session = self.get_cursor()
        record = self._get_Car_by_Reg_num(CarRegNum)
        if not hasattr(record, 'CarRegNum'):
            car = Cars(
                CarRegNum=CarRegNum,
                CarMakeID=CarMakeID,
                CarType=CarType)
            session.add(car)
            session.commit()

    def read_Car(self,):
        session = self.get_cursor()
        record = session.query(Cars).all()
        return self.list2dict(record)

    def update_Car(self, CarRegNum, CarMakeID, CarType):
        session = self.get_cursor()
        record = self._get_Car_by_Reg_num(CarRegNum)
        if hasattr(record, 'CarRegNum'):
            record.CarMakeID = CarMakeID
            record.CarTypeID = CarType
            session.commit()

    def del_Car(self, CarRegNum):
        session = self.get_cursor()
        car = self._get_Car_by_Reg_num(CarRegNum)
        session.delete(car)
        session.commit()

        # Parking

    def _get_parking_place_by_id(self, ParkingPlaceID):
        session = self.get_cursor()
        record = session.query(ParkingPlace).filter_by(
            ParkingPlaceID=ParkingPlaceID).first()
        return record

    def get_parking_place_by_id(self, ParkingPlaceID):
        return self.get_parking_place_by_id(ParkingPlaceID).to_dict()

    def create_parking_place(self, ParkingPlaceID, ParkingPlaceDesc=''):
        session = self.get_cursor()
        record = self._get_parking_place_by_id(ParkingPlaceID)
        if not hasattr(record, 'ParkingPlaceID'):
            parkingplace = ParkingPlace(
                ParkingPlaceID=ParkingPlaceID,
                ParkingPlaceDesc=ParkingPlaceDesc)
            session.add(parkingplace)
            session.commit()

    def read_parking_place(self,):
        session = self.get_cursor()
        record = session.query(ParkingPlace).all()
        return self.list2dict(record)

    def update_parking_place(self, ParkingPlaceID, ParkingPlaceDesc=''):
        session = self.get_cursor()
        record = self._get_parking_place_by_id(ParkingPlaceID)
        if hasattr(record, 'ParkingPlaceID'):
            record.ParkingPlaceDesc = ParkingPlaceDesc
            session.commit()

    def del_parking_place(self, ParkingPlaceID):
        session = self.get_cursor()
        ParkingPlace.query.filter(
            ParkingPlace.ParkingPlaceID == ParkingPlaceID).delete()
        session.commit()

    def get_free_parking_place(self):
        cursor = self.get_cursor()
        query = 'select "ParkingPlaceID", "ParkingPlaceDesc" from public."ParkingPlace" where "ParkingPlaceID" not in (select "ParkingID" from public."Contract" where "ContractEnd" >= (SELECT CURRENT_DATE))'
        cursor.execute(query)
        self._connection.commit()
        record = cursor.fetchall()
        return record

        def chek_parking_place(self, id):
            cursor = self.get_cursor()
            query = 'select "ParkingPlaceID", "ParkingPlaceDesc" from public."ParkingPlace" where "ParkingPlaceID" not in (select "ParkingID" from public."Contract" where "ContractEnd" >= (SELECT CURRENT_DATE)) and "ParkingPlaceID" = ' + str(
                id)
            cursor.execute(query)
            self._connection.commit()
            record = cursor.fetchone()
            return record

    ########Person

    def _get_person_by_last_name(self, PersonLastName):
        session = self.get_cursor()
        record = session.query(Persons).filter_by(
            PersonLastName=PersonLastName).first()
        return record

    def get_person_by_last_name(self, PersonLastName):
        return self._get_person_by_last_name(self, PersonLastName).to_dict()

    def _get_person_by_id(self, PersonID):
        session = self.get_cursor()
        record = session.query(Persons).filter_by(
            PersonID=PersonID).first()
        return record

    def get_person_by_id(self, PersonID):
        return self._get_person_by_id(self, PersonID).to_dict()

    def create_person(self, PersonID, PersonLastName, PersonName, PersonMidleName):
        session = self.get_cursor()
        record = self._get_person_by_id(PersonID)
        if not hasattr(record, 'PersonID'):
            person = Persons(
                PersonID=PersonID,
                PersonLastName=PersonLastName,
                PersonName=PersonName,
                PersonMidleName=PersonMidleName)
            session.add(person)
            session.commit()

    def read_person(self,):
        session = self.get_cursor()
        record = session.query(Persons).all()
        return self.list2dict(record)

    def update_person(self, PersonID, PersonLastName, PersonName, PersonMidleName):
        session = self.get_cursor()
        record = self._get_person_by_id(PersonID)
        if hasattr(record, 'PersonID'):
            record.PersonLastName = PersonLastName
            record.PersonName = PersonName
            record.PersonMidleName = PersonMidleName
            session.commit()

    def del_person(self, PersonID):
        session = self.get_cursor()
        record = self._get_person_by_id(PersonID)
        session.delete(record)
        session.commit()

    #######Phones
    def _get_phones_by_phones(self, Phone):
        session = self.get_cursor()
        record = session.query(Phones).filter_by(
            Phone=Phone).first()
        return record

    def get_phones_by_phones(self, Phone):
        return self._get_phones_by_phones(self, Phone).to_dict()

    def create_phones(self, PersonID, Phone):
        session = self.get_cursor()
        record = self._get_phones_by_phones(Phone)
        if not hasattr(record, 'Phone'):
            phone = Phones(
                Phone=Phone,
                PersonID=PersonID)
            session.add(phone)
            session.commit()

    def read_phones(self,):
        session = self.get_cursor()
        record = session.query(Phones).all()
        return self.list2dict(record)

    def update_phones(self, PersonID, Phone):
        session = self.get_cursor()
        record = self._get_phones_by_phones(Phone)
        if hasattr(record, 'Phone'):
            record.PersonID = PersonID
            record.Phone = Phone
            session.commit()

    def del_phones(self, Phone):
        session = self.get_cursor()
        Phones.query.filter(
            Phones.Phone == Phone).delete()
        session.commit()

    ####### Contracts

    def _get_contract_by_PersonID(self, PersonID):
        session = self.get_cursor()
        record = session.query(Contract).filter_by(PersonID=PersonID).all()
        return record

    def get_contract_by_PersonID(self, PersonID):
        return self.list2dict(self._get_contract_by_PersonID(self, PersonID))

    def _get_currentContract_by_carRegNum(self, CarNumber):
        session = self.get_cursor()
        query = session.query(Contract, Cars, CarType, Makes, Persons)
        query = query.join(Cars, Cars.CarRegNum == Contract.CarNumber)
        query = query.join(CarType, Cars.CarType == CarType.CarTypeID)
        query = query.join(Makes, Cars.CarMakeID == Makes.MakeID)
        query = query.join(Persons, Persons.PersonID == Contract.PersonID)
        query = query.filter(Contract.CarNumber == CarNumber,
                             Contract.ContractEnd == '2022-05-02')
        record = query.first()
        return record

    def get_currentContract_by_carRegNum(self, CarNumber):
        return self.sqlaRecord2dict(self._get_currentContract_by_carRegNum(CarNumber))

    def _get_contract_by_ParkingID(self, ParkingID):
        session = self.get_cursor()
        record = session.query(Parking).filter_by(ParkingID=ParkingID).all()
        return record

    def get_contract_by_ParkingID(self, ParkingID):
        return self.list2dict(self._get_contract_by_ParkingID(self, ParkingID))

    def _get_contract_by_ContractID(self, ContractID):
        session = self.get_cursor()
        record = session.query(Contract).filter_by(
            ContractID=ContractID).first()
        return record

    def get_contract_by_ContractID(self, ContractID):
        return self._get_contract_by_ContractID(self, ContractID).to_dict()

    def close_contract(self, id):
        session = self.get_cursor()
        record = self._get_contract_by_ContractID(id)
        if hasattr(record, 'ContractID'):
            record.ContractEnd = date.today()
            session.commit()

    def create_contract(self, CarNumber, PersonID, ParkingID, ContractEnd):
        session = self.get_cursor()
        contract = Contract(
                CarNumber=CarNumber,
                PersonID=PersonID,
                ParkingID=ParkingID,
                ContractEnd=ContractEnd)
        session.add(contract)
        session.commit()

    def read_contract(self,):
        session = self.get_cursor()
        query = session.query(Contract, Cars, CarType, Makes, Persons)
        query = query.join(Cars, Cars.CarRegNum == Contract.CarNumber)
        query = query.join(CarType, Cars.CarType == CarType.CarTypeID)
        query = query.join(Makes, Cars.CarMakeID == Makes.MakeID)
        query = query.join(Persons, Persons.PersonID == Contract.PersonID)
        record = query.all()
        return self.sqlaListRecordsToDict(record)

    def update_contract(self, ContractID, CarNumber, PersonID, ParkingID, ContractStart, ContractEnd):
        session = self.get_cursor()
        record = self._get_contract_by_ContractID(ContractID)
        if hasattr(record, 'ContractID'):
            record.PersonID = PersonID
            record.CarNumber = CarNumber
            record.ParkingID = ParkingID
            record.ContractStart = ContractStart
            record.ContractEnd = ContractEnd
            session.commit()

    def del_contract_by_temp_table_CarNum(self, CarNum):
        session = self.get_cursor()
        car = self._get_Car_by_Reg_num(CarNum)
        contracts = self._get_currentContract_by_carRegNum(CarNum)
        for c in contracts:
            cars.person.remove(c)
        session.commit()
        self.del_Car(CarNum)

    def del_contract_by_temp_table_personID(self, personID):
        session = self.get_cursor()
        person = self._get_person_by_id(personID)
        contracts = self._get_contract_by_PersonID(personID)
        for c in contracts:
            person.cars.remove(c)
        session.commit()
        self.del_person(personID)

    def del_contract_by_temp_table_ContractID(self, ContractID):
        session = self.get_cursor()
        contract = self._get_contract_by_ContractID(ContractID)
        person = self._get_person_by_id(contract.PersonID)
        person.cars.remove(contract)
        session.commit()

    def random_create(self, param):
        session = self.get_cursor()
        session.execute('public.generate_data ?', [param])
        session.commit()

    #CREATE OR REPLACE PROCEDURE generate_data(dataCount integer)
    #AS $$
    #
    #DECLARE
    #  i SMALLINT;
    #  Persons RECORD;
    #  CarNum text;
    #
    #BEGIN
    #  INSERT INTO public."Persons" ("PersonID","PersonLastName","PersonMidleName","PersonName")
    #    SELECT floor(10000000000+random()*89999999999)::bigint,
    #      chr(floor(65 + random()*25)::int) ||
    #      chr(floor(97 + random()*25)::int) || chr(floor(97 + random()*25)::int) ||
    #      chr(floor(97 + random()*25)::int) || chr(floor(97 + random()*25)::int) ||
    #      chr(floor(97 + random()*25)::int),
    #      chr(floor(65 + random()*25)::int) ||
    #      chr(floor(97 + random()*25)::int) || chr(floor(97 + random()*25)::int) ||
    #      chr(floor(97 + random()*25)::int) || chr(floor(97 + random()*25)::int) ||
    #      chr(floor(97 + random()*25)::int) || chr(floor(97 + random()*25)::int) ||
    #      chr(floor(97 + random()*25)::int),
    #      chr(floor(65 + random()*25)::int) ||
    #      chr(floor(97 + random()*25)::int) || chr(floor(97 + random()*25)::int) ||
    #      chr(floor(97 + random()*25)::int) || chr(floor(97 + random()*25)::int) ||
    #      chr(floor(97 + random()*25)::int) || chr(floor(97 + random()*25)::int) ||
    #      chr(floor(97 + random()*25)::int)
    #    FROM generate_series(1, dataCount);
    #
    #  FOR Persons IN
    #      SELECT "PersonID" from public."Persons" where "PersonID" not in (SELECT DISTINCT "PersonID" from public."Contract")
    #     LOOP
    #      CarNum :=(chr(floor(65 + random()*25)::int) ||
    #      chr(floor(65 + random()*25)::int) || floor( random()*9)::int ||
    #      floor( random()*9)::int || floor( random()*9)::int || floor( random()*9)::int || chr(floor(65 + random()*25)::int) ||
    #      chr(floor(65 + random()*25)::int));
    #      INSERT INTO public."Cars" ("CarMakeID","CarRegNum","CarType")
    #    SELECT  (select "MakeID" from public."Makes" where "MakeID" >= (select floor(random()* (SELECT MAX("MakeID") FROM public."Makes"))::int) limit 1) ,
    #      CarNum,
    #      (SELECT  "CarTypeID" FROM public."CarType" ORDER BY random() LIMIT 1);
    #
    #    insert into public."Contract" ("CarNumber","ContractStart","ContractEnd","ParkingID","PersonID")
    #         select
    #              CarNum,
    #                 (SELECT CURRENT_DATE - 1 -(30 * floor( random()*12)::int) ) ,
    #                 (SELECT CURRENT_DATE + 30 * floor( random()*12)::int ),
    #                    floor( 1+ random()*9999)::int,
    #                    Persons."PersonID";
    #  END LOOP;
    #END;
    #$$ LANGUAGE plpgsql;

    def select(self, parking_start, parking_end, PersonPart, Date):
        session = self.get_cursor()
        query = session.query(Contract, Cars, CarType, Makes, Persons)
        query = query.join(Cars, Cars.CarRegNum == Contract.CarNumber)
        query = query.join(CarType, Cars.CarType == CarType.CarTypeID)
        query = query.join(Makes, Cars.CarMakeID == Makes.MakeID)
        query = query.join(Persons, Persons.PersonID == Contract.PersonID)
        query = query.filter(Contract.ParkingID.between(parking_start, parking_end),
                             Persons.PersonLastName.like(PersonPart),
                             Contract.ContractEnd > Date)
        record = query.all()
        #print(type(record))
        print(record)
        return self.sqlaListRecordsToDict(record)

    def clear_data(self):
        return dict(ContractID='',
                    CarNumber='',
                    ParkingID='',
                    PersonID='',
                    ContractStart='',
                    ContractEnd='',
                    CarMakeID='',
                    CarType='',
                    CarTypeName='',
                    MakeName='',
                    PersonLastName='',
                    PersonName='',
                    PersonMidleName='')
