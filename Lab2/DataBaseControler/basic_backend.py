import mvc_exceptions as mvc_exc
import psycopg
from psycopg import Error
from psycopg.rows import dict_row

items = list()
 

_connection = None
_cursor = None


def get_connection():
    global _connection
    if not _connection:
        _connection = psycopg.connect("user=ivan password=12345678 host=ubuntu.ivan.zeleniak.net port=5432 dbname=Parking",row_factory=dict_row)
    return _connection


def get_cursor():
    global _cursor
    if _cursor:
        return _cursor
    else:
        connection = get_connection()
        _cursor = connection.cursor(row_factory=dict_row)
        return _cursor


def get_make_by_name (makeName):
    cursor = get_cursor()
    query = 'SELECT * FROM public."Makes" WHERE "MakeName" ='+"'" + str(makeName)+"'"
    cursor.execute(query)
    _connection.commit()
    record = cursor.fetchone()
    return record


def get_make_by_id (makeID):
    cursor = get_cursor()
    query = 'select * from public."Makes" where "MakeID" ='+"'" + str(makeID)+"'"
    cursor.execute(query)
    _connection.commit()
    record = cursor.fetchone()
    return record


def create_make (makeName,MakeDescription=''):
    cursor = get_cursor()
    record = get_make_by_name(makeName)
    if cursor.rowcount == 0:
        query = 'INSERT INTO public."Makes"("MakeName", "MakeDescription")' + "VALUES ('"+ str(makeName)+"','"+ str(MakeDescription)+"');"
        cursor.execute(query)
        
        _connection.commit()
    else:
        makeid = record["MakeID"]
    return makeid

def read_make ():
    cursor = get_cursor()
    query = 'SELECT "MakeID", "MakeName", "MakeDescription" FROM public."Makes";'
    cursor.execute(query)
    _connection.commit()
    record = cursor.fetchall()
    return record

def update_make (MakeID,MakeName,MakeDescription=''):
    cursor = get_cursor()
    record = get_make_by_id(MakeID)
    if cursor.rowcount > 0:
        query = 'UPDATE public."Makes"	SET  "MakeName"='+"'"+str(MakeName) +"'"+', "MakeDescription"='+"'"+str(MakeDescription) +"'"+ '	WHERE "MakeID" = '+ str(MakeID)+ ' ;'
        cursor.execute(query)
        _connection.commit()


def del_make (MakeID):
    cursor = get_cursor()
    record = get_make_by_id(MakeID)
    if cursor.rowcount > 0:
        query = 'DELETE FROM public."Makes"	WHERE "MakeID"='+ str(MakeID)+ ';'
        cursor.execute(query)
        _connection.commit()


######Type
def get_CarType_by_name (CarTypeName):
    cursor = get_cursor()
    query = 'SELECT * FROM public."CarType" WHERE "CarTypeName" ='+"'" + str(CarTypeName)+"'"
    cursor.execute(query)
    _connection.commit()
    record = cursor.fetchone()
    return record


def get_CarType_by_id (CarTypeID):
    cursor = get_cursor()
    query = 'select * from public."CarType" where "CarTypeID" ='+"'" + str(CarTypeID)+"'"
    cursor.execute(query)
    _connection.commit()
    record = cursor.fetchone()
    return record

def create_temp_table():
    cursor = get_cursor()
    query = '''DROP TABLE IF EXISTS public."TMP_Contract";
    CREATE TABLE IF NOT EXISTS public."TMP_Contract"
    (
    "ContractID" smallint NOT NULL,
    "CarNumber" character varying(8) COLLATE pg_catalog."default" NOT NULL,
    "PersonID" bigint NOT NULL,
    "ParkingID" smallint NOT NULL,
    "ContractStart" date NOT NULL,
    "ContractEnd" date NOT NULL
    );'''
    cursor.execute(query)
    _connection.commit()

def del_contract_by_temp_table_CarNum(CarNum):
    cursor = get_cursor()
    query ='''insert into public."TMP_Contract" ("ContractID","PersonID","CarNumber","ParkingID","ContractStart","ContractEnd") select "ContractID","PersonID","CarNumber","ParkingID","ContractStart","ContractEnd" from public."Contract" where "CarNumber"='''+CarNum  +''';
    delete from public."Contract" where "ContractID" in (select distinct "ContractID" from public."TMP_Contract" )
    delete from public."Cars" where "CarRegNum" = ''' + CarNum + ";"+'''
    delete from public."Persons" where "PersonID" in (select distinct "PersonID" from public."TMP_Contract" ) and "PersonID" not in (select distinct "PersonID" from public."Contract" where "PersonID"  in (select distinct "PersonID" from public."TMP_Contract" ) )'''

    cursor.execute(query)
    _connection.commit()
    del_temp_table()

def del_contract_by_temp_table_personID(personID):
    cursor = get_cursor()
    query ='''insert into public."TMP_Contract" ("ContractID","PersonID","CarNumber","ParkingID","ContractStart","ContractEnd") select "ContractID","PersonID","CarNumber","ParkingID","ContractStart","ContractEnd" from public."Contract" where "PersonID"='''+personID  +''';
    delete from public."Contract" where "ContractID" in (select distinct "ContractID" from public."TMP_Contract" )
    delete from public."Cars" where "CarRegNum" = (select distinct "CarRegNum" from public."TMP_Contract" )
    delete from public."Persons" where "PersonID" = ''' + personID + ";"
    cursor.execute(query)
    _connection.commit()
    del_temp_table()




def del_temp_table():
    cursor = get_cursor()
    query ='''DROP TABLE IF EXISTS public."TMP_Contract";'''
    cursor.execute(query)
    _connection.commit()


def create_CarType (CarTypeName):
    cursor = get_cursor()
    record = get_CarType_by_name(CarTypeName)
    if cursor.rowcount == 0:
        query = 'INSERT INTO public."CarType"("CarTypeName")' + "VALUES ('"+ str(CarTypeName)+"');"
        cursor.execute(query)
        _connection.commit()


def read_CarType ():
    cursor = get_cursor()
    query = 'SELECT "CarTypeID", "CarTypeName" FROM public."CarType" ; '
    cursor.execute(query)
    _connection.commit()
    record = cursor.fetchall()
    return record

def update_CarType (CarTypeID,CarTypeName):
    cursor = get_cursor()
    record = get_CarType_by_id(CarTypeID)
    if cursor.rowcount > 0:
        query = 'UPDATE public."CarType"	SET  "CarTypeName"='+"'"+str(CarTypeName) +"'"+'	WHERE "CarTypeID" = '+ str(CarTypeID)+ ' ;'
        cursor.execute(query)
        _connection.commit()


def del_CarType (CarTypeID):
    cursor = get_cursor()
    record = get_CarType_by_id(CarTypeID)
    if cursor.rowcount > 0:
        query = 'DELETE FROM public."CarType"	WHERE "CarTypeID"='+ str(CarTypeID)+ ';'
        cursor.execute(query)
        _connection.commit()



########Cars

def get_Car_by_Reg_num (CarRegNum):
    cursor = get_cursor()
    query = 'SELECT * FROM public."Cars" WHERE "CarRegNum" ='+"'" + str(CarRegNum)+"'"
    cursor.execute(query)
    _connection.commit()
    record = cursor.fetchone()
    return record




def create_Car (CarRegNum,CarMakeID,CarType):
    cursor = get_cursor()
    record = get_Car_by_Reg_num(CarRegNum)
    if cursor.rowcount == 0:
        query = 'INSERT INTO public."Cars"("CarRegNum", "CarMakeID" , "CarType")' + "VALUES ('"+ str(CarRegNum)+"',"+ str(CarMakeID)+","+ str(CarType) +"');"
        cursor.execute(query)
        
        _connection.commit()
    else:
        makeid = record[0]
    return makeid

def read_Car ():
    cursor = get_cursor()
    query = 'SELECT "CarRegNum", "CarMakeID", "CarType" FROM public."Cars";'
    cursor.execute(query)
    _connection.commit()
    record = cursor.fetchall()
    return record

def update_Car (CarRegNum,CarMakeID,CarType):
    cursor = get_cursor()
    record = get_Car_by_Reg_num(CarRegNum)
    if cursor.rowcount > 0:
        query = 'UPDATE public."Cars"	SET  "CarType"='+"'"+str(CarType) +"'"+', "CarMakeID"='+"'"+str(CarMakeID) +"'"+ '	WHERE "CarRegNum" = '+ str(CarRegNum)+ ' ;'
        cursor.execute(query)
        _connection.commit()


def del_Car (CarRegNum):
    cursor = get_cursor()
    record = get_Car_by_Reg_num(CarRegNum)
    if cursor.rowcount > 0:
        query = 'DELETE FROM public."Cars"	WHERE "CarRegNum"='+ str(CarRegNum)+ ';'
        cursor.execute(query)
        _connection.commit()


##########Parking


def get_parking_place_by_id (ParkingPlaceID):
    cursor = get_cursor()
    query = 'select * from public."ParkingPlace" where "ParkingPlaceID" ='+"'" + str(ParkingPlaceID)+"'"
    cursor.execute(query)
    _connection.commit()
    record = cursor.fetchone()
    return record


def create_parking_place (ParkingPlaceID,ParkingPlaceDesc=''):
    cursor = get_cursor()
    record = get_parking_place_by_id(ParkingPlaceID)
    if cursor.rowcount == 0:
        query = 'INSERT INTO public."ParkingPlace"("ParkingPlaceID", "ParkingPlaceDesc")' + "VALUES ('"+ str(ParkingPlaceID)+"','"+ str(ParkingPlaceDesc)+"');"
        cursor.execute(query)
        ParkingPlaceid=cursor.lastrowid
        _connection.commit()
    else:
        ParkingPlaceid = record[0]
    return ParkingPlaceid

def read_parking_place ():
    cursor = get_cursor()
    query = 'SELECT "ParkingPlaceID",  "ParkingPlaceDesc" FROM public."ParkingPlace";'
    cursor.execute(query)
    _connection.commit()
    record = cursor.fetchall()
    return record

def update_parking_place (ParkingPlaceID,ParkingPlaceDesc=''):
    cursor = get_cursor()
    record = get_parking_place_by_id(ParkingPlaceID)
    if cursor.rowcount > 0:
        query = 'UPDATE public."ParkingPlace"	SET ' +', "ParkingPlaceDesc"='+"'"+str(ParkingPlaceDesc) +"'"+ '	WHERE "ParkingPlaceID" = '+ str(ParkingPlaceID)+ ' ;'
        cursor.execute(query)
        _connection.commit()


def del_parking_place (ParkingPlaceID):
    cursor = get_cursor()
    record = get_parking_place_by_id(ParkingPlaceID)
    if cursor.rowcount > 0:
        query = 'DELETE FROM public."ParkingPlace"	WHERE "ParkingPlaceID"='+ str(ParkingPlaceID)+ ';'
        cursor.execute(query)
        _connection.commit()

########Person


def get_person_by_last_name (PersonLastName):
    cursor = get_cursor()
    query = 'SELECT * FROM public."Persons" WHERE "PersonLastName" ='+"'" + str(PersonLastName)+"'"
    cursor.execute(query)
    _connection.commit()
    record = cursor.fetchone()
    return record


def get_person_by_id (PersonID):
    cursor = get_cursor()
    query = 'select * from public."Persons" where "PersonID" ='+"'" + str(PersonID)+"'"
    cursor.execute(query)
    _connection.commit()
    record = cursor.fetchone()
    return record


def create_person (PersonID, PersonLastName, PersonName,PersonMidleName):
    cursor = get_cursor()
    record = get_person_by_id(PersonID)
    if cursor.rowcount == 0:
        query = 'INSERT INTO public."Persons"("PersonID", "PersonLastName", "PersonName" , "PersonMidleName" )' + "VALUES ('"+ str(PersonID), str(PersonLastName), str(PersonName),str(PersonMidleName) +"');"
        cursor.execute(query)
        
        _connection.commit()
    else:
        makeid = record[0]
    return makeid

def read_person ():
    cursor = get_cursor()
    query = 'SELECT "PersonID", "PersonLastName", "PersonName","PersonMidleName" FROM public."Persons";'
    cursor.execute(query)
    _connection.commit()
    record = cursor.fetchall()
    return record

def update_person (PersonID, PersonLastName, PersonName,PersonMidleName):
    cursor = get_cursor()
    record = get_person_by_id(PersonID)
    if cursor.rowcount > 0:
        query = 'UPDATE public."Persons" SET "PersonLastName"='+"'"+str(PersonLastName) +"'"+'"PersonName"='+"'"+str(PersonName) +"'"+', "PersonMidleName"='+"'"+str(PersonMidleName) +"'"+ '	WHERE "PersonID" = '+ str(PersonID)+ ' ;'
        cursor.execute(query)
        _connection.commit()


def del_person (PersonID):
    cursor = get_cursor()
    record = get_person_by_id(PersonID)
    if cursor.rowcount > 0:
        query = 'DELETE FROM public."Persons"	WHERE "PersonID"='+ str(PersonID)+ ';'
        cursor.execute(query)
        _connection.commit()

#######Phones
def get_phones_by_phone (Phone):
    cursor = get_cursor()
    query = 'select * from public."Phones" where "Phone" ='+"'" + str(Phone)+"'"
    cursor.execute(query)
    _connection.commit()
    record = cursor.fetchone()
    return record


def chek_parking_place(id):
    cursor = get_cursor()
    query = 'select "ParkingPlaceID", "ParkingPlaceDesc" from public."ParkingPlace" where "ParkingPlaceID" not in (select "ParkingID" from public."Contract" where "ContractEnd" >= (SELECT CURRENT_DATE)) and "ParkingPlaceID" = '+ str(id)
    cursor.execute(query)
    _connection.commit()
    record = cursor.fetchone()
    return record


def get_free_parking_place():
    cursor = get_cursor()
    query = 'select "ParkingPlaceID", "ParkingPlaceDesc" from public."ParkingPlace" where "ParkingPlaceID" not in (select "ParkingID" from public."Contract" where "ContractEnd" >= (SELECT CURRENT_DATE))'
    cursor.execute(query)
    _connection.commit()
    record = cursor.fetchall()
    return record


def create_phones (PersonID,Phone):
    cursor = get_cursor()
    record = get_phones_by_phone(Phone)
    if cursor.rowcount == 0:
        query = 'INSERT INTO public."Phones"("PersonID", "Phone")' + "VALUES ('"+ str(PersonID)+"','"+ str(Phone)+"');"
        cursor.execute(query)
        
        _connection.commit()
    else:
        makeid = record[0]
    return makeid

def read_phones ():
    cursor = get_cursor()
    query = 'SELECT "PersonID", "Phone" FROM public."Phones";'
    cursor.execute(query)
    _connection.commit()
    record = cursor.fetchall()
    return record

def update_phones (PersonID,Phone):
    cursor = get_cursor()
    record = get_phones_by_phones(Phone)
    if cursor.rowcount > 0:
        query = 'UPDATE public."Phones"	SET , "PersonID"='+"'"+str(PersonID) +"'"+ '	WHERE "Phone" = '+ str(Phone)+ ' ;'
        cursor.execute(query)
        _connection.commit()


def del_phones (Phone):
    cursor = get_cursor()
    record = get_phones_by_phones(Phone)
    if cursor.rowcount > 0:
        query = 'DELETE FROM public."Phones"	WHERE "Phone"='+ str(Phone)+ ';'
        cursor.execute(query)
        _connection.commit()

####### Contracts

def get_contract_by_PersonID (PersonID):
    cursor = get_cursor()
    query = 'SELECT * FROM public."Contract" WHERE "PersonID" ='+"'" + str(PersonID)+"'"
    cursor.execute(query)
    _connection.commit()
    record = cursor.fetchone()
    return record

def clear_data():
    cursor = get_cursor()
    query = ''' select '' as  "ContractID", '' as "CarNumber", '' as "ParkingID", '' as "PersonID", '' as "ContractStart", '' as "ContractEnd", '' as "CarMakeID", '' as "CarType", '' as "CarTypeName", '' as "MakeName", '' as "PersonLastName", '' as "PersonName", '' as "PersonMidleName"'''
    cursor.execute(query)
    _connection.commit()
    record = cursor.fetchone()
    return record


def get_currentContract_by_carRegNum(CarNumber):
    cursor = get_cursor()
    query = '''select "ContractID", "CarNumber", "ParkingID", "Contract"."PersonID" as "PersonID", "ContractStart", "ContractEnd","CarMakeID","CarType", "CarTypeName", "MakeName", "PersonLastName", "PersonName", "PersonMidleName"
                from public."Contract" 
	                INNER JOIN public."Cars" on public."Contract"."CarNumber" = public."Cars"."CarRegNum" 
	                INNER JOIN public."CarType" on public."Cars"."CarType" = public."CarType"."CarTypeID"
	                INNER JOIN public."Makes" on public."Makes"."MakeID" = public."Cars"."CarMakeID"
	                INNER JOIN public."Persons" on public."Persons"."PersonID" = public."Contract"."PersonID"
	            where "ContractID"=(select max("ContractID") from public."Contract" where "CarNumber" = \'''' + str(CarNumber)+"')"
    cursor.execute(query)
    _connection.commit()
    record = cursor.fetchone()
    return record


def get_contract_by_ParkingID (ParkingID):
    cursor = get_cursor()
    query = 'select * from public."Contract" where "ParkingID" ='+"'" + str(ParkingID)+"'"
    cursor.execute(query)
    _connection.commit()
    record = cursor.fetchone()
    return record


def get_contract_by_ContractID (ContractID):
    cursor = get_cursor()
    query = 'select * from public."Contract" where "ContractID" ='+"'" + str(ContractID)+"'"
    cursor.execute(query)
    _connection.commit()
    record = cursor.fetchone()
    return record


def create_contract (CarNumber,PersonID,ParkingID,days):
    cursor = get_cursor()
    query = 'INSERT INTO public."Contract"("CarNumber","PersonID","ParkingID","ContractStart","ContractEnd")' + "VALUES ('"+ str(CarNumber)+"',"+str(PersonID)+","+str(ParkingID)+","+"(SELECT CURRENT_DATE) " +","+"(SELECT CURRENT_DATE +"+str(days)+"));"
    cursor.execute(query)
    
    _connection.commit()
    return makeid

def close_contract(ContractID):
     cursor = get_cursor()
     query = 'UPDATE public."Contract"	SET  "ContractEnd"= (SELECT CURRENT_DATE-1)  WHERE "ContractID" = '+ str(ContractID)+ ' ;'
     cursor.execute(query)
     _connection.commit()

def read_contract ():
    cursor = get_cursor()
    query = 'SELECT "CarNumber","PersonID","ParkingID","ContractStart","ContractEnd" FROM public."Contract";'
    cursor.execute(query)
    _connection.commit()
    record = cursor.fetchall()
    return record

def update_contract (ContractID,CarNumber,PersonID,ParkingID,ContractStart,ContractEnd):
    cursor = get_cursor()
    record = get_contract_by_ContractID(ContractID)
    if cursor.rowcount > 0:
        query = 'UPDATE public."Contract"	SET  "CarNumber"='+"'"+str(CarNumber) +"'"+', "PersonID"='+"'"+str(PersonID) +"'"+', "ParkingID"='+"'"+str(ParkingID)+"'"+ ', "ContractStart"='+"'"+str(ContractStart) +"'"+ ', "ContractEnd"='+"'"+str(ContractEnd) +"'"+'	WHERE "ContractID" = '+ str(ContractID)+ ' ;'
        cursor.execute(query)
        _connection.commit()


def del_contract (ContractID):
    cursor = get_cursor()
    record = get_contract_by_ContractID(ContractID)
    if cursor.rowcount > 0:
        query = 'DELETE FROM public."Contract"	WHERE "ContractID"='+ str(ContractID)+ ';'
        cursor.execute(query)
        _connection.commit()