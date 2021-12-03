import mvc_exceptions as mvc_exc
import psycopg
from psycopg import Error
from psycopg.rows import dict_row


class ModelBasic(object):

    _connection = None
    _cursor = None

    def get_connection(self):
        
        if not self._connection:
            self._connection = psycopg.connect("user=ivan password=12345678 host=ubuntu.ivan.zeleniak.net port=5432 dbname=Parking",row_factory=dict_row)
        return self._connection
    
    
    def get_cursor(self):
        
        if self._cursor:
            return self._cursor
        else:
            connection = self.get_connection()
            self._cursor = connection.cursor(row_factory=dict_row)
            return self._cursor
    


    def get_make_by_name (self ,makeName):
        cursor = self.get_cursor()
        query = 'SELECT * FROM public."Makes" WHERE "MakeName" ='+"'" + str(makeName)+"'"
        cursor.execute(query)
        self._connection.commit()
        record = cursor.fetchone()
        return record
    
    
    def get_make_by_id (self ,makeID):
        cursor = self.get_cursor()
        query = 'select * from public."Makes" where "MakeID" ='+"'" + str(makeID)+"'"
        cursor.execute(query)
        self._connection.commit()
        record = cursor.fetchone()
        return record
    
    
    
    def create_make (self ,makeName,MakeDescription=''):
        cursor = self.get_cursor()
        record = get_make_by_name(makeName)
        if cursor.rowcount == 0:
            query = 'INSERT INTO public."Makes"("MakeName", "MakeDescription")' + "VALUES ('"+ str(makeName)+"','"+ str(MakeDescription)+"');"
            cursor.execute(query)
            
            self._connection.commit()
        else:
            makeid = record["MakeID"]
        return makeid
    
    def read_make (self ,):
        cursor = self.get_cursor()
        query = 'SELECT "MakeID", "MakeName", "MakeDescription" FROM public."Makes";'
        cursor.execute(query)
        self._connection.commit()
        record = cursor.fetchall()
        return record
    
    def update_make (self ,MakeID,MakeName,MakeDescription=''):
        cursor = self.get_cursor()
        record = get_make_by_id(MakeID)
        if cursor.rowcount > 0:
            query = 'UPDATE public."Makes"	SET  "MakeName"='+"'"+str(MakeName) +"'"+', "MakeDescription"='+"'"+str(MakeDescription) +"'"+ '	WHERE "MakeID" = '+ str(MakeID)+ ' ;'
            cursor.execute(query)
            self._connection.commit()
    
    
    def del_make (self ,MakeID):
        cursor = self.get_cursor()
        record = get_make_by_id(MakeID)
        if cursor.rowcount > 0:
            query = 'DELETE FROM public."Makes"	WHERE "MakeID"='+ str(MakeID)+ ';'
            cursor.execute(query)
            self._connection.commit()
    


##############Type


    def get_CarType_by_name (self ,CarTypeName):
        cursor = self.get_cursor()
        query = 'SELECT * FROM public."CarType" WHERE "CarTypeName" ='+"'" + str(CarTypeName)+"'"
        cursor.execute(query)
        self._connection.commit()
        record = cursor.fetchone()
        return record
    
    
    def get_CarType_by_id (self ,CarTypeID):
        cursor = self.get_cursor()
        query = 'select * from public."CarType" where "CarTypeID" ='+"'" + str(CarTypeID)+"'"
        cursor.execute(query)
        self._connection.commit()
        record = cursor.fetchone()
        return record
            
        
    
    def create_CarType (self ,CarTypeName):
        cursor = self.get_cursor()
        record = get_CarType_by_name(CarTypeName)
        if cursor.rowcount == 0:
            query = 'INSERT INTO public."CarType"("CarTypeName")' + "VALUES ('"+ str(CarTypeName)+"');"
            cursor.execute(query)
            self._connection.commit()
    
    
    def read_CarType (self ,):
        cursor = self.get_cursor()
        query = 'SELECT "CarTypeID", "CarTypeName" FROM public."CarType" ; '
        cursor.execute(query)
        self._connection.commit()
        record = cursor.fetchall()
        return record
    
    def update_CarType (self ,CarTypeID,CarTypeName):
        cursor = self.get_cursor()
        record = get_CarType_by_id(CarTypeID)
        if cursor.rowcount > 0:
            query = 'UPDATE public."CarType"	SET  "CarTypeName"='+"'"+str(CarTypeName) +"'"+'	WHERE "CarTypeID" = '+ str(CarTypeID)+ ' ;'
            cursor.execute(query)
            self._connection.commit()
    
    
    def del_CarType (self ,CarTypeID):
        cursor = self.get_cursor()
        record = get_CarType_by_id(CarTypeID)
        if cursor.rowcount > 0:
            query = 'DELETE FROM public."CarType"	WHERE "CarTypeID"='+ str(CarTypeID)+ ';'
            cursor.execute(query)
            self._connection.commit()



    ########Cars
    
    def get_Car_by_Reg_num (self ,CarRegNum):
        cursor = self.get_cursor()
        query = 'SELECT * FROM public."Cars" WHERE "CarRegNum" ='+"'" + str(CarRegNum)+"'"
        cursor.execute(query)
        self._connection.commit()
        record = cursor.fetchone()
        return record
    
    
    
    
    def create_Car (self ,CarRegNum,CarMakeID,CarType):
        cursor = self.get_cursor()
        record = get_Car_by_Reg_num(CarRegNum)
        if cursor.rowcount == 0:
            query = 'INSERT INTO public."Cars"("CarRegNum", "CarMakeID" , "CarType")' + "VALUES ('"+ str(CarRegNum)+"',"+ str(CarMakeID)+","+ str(CarType) +");"
            cursor.execute(query)
            
            self._connection.commit()
        else:
            makeid = record[0]
    
    def read_Car (self ,):
        cursor = self.get_cursor()
        query = 'SELECT "CarRegNum", "CarMakeID", "CarType" FROM public."Cars";'
        cursor.execute(query)
        self._connection.commit()
        record = cursor.fetchall()
        return record
    
    def update_Car (self ,CarRegNum,CarMakeID,CarType):
        cursor = self.get_cursor()
        record = get_Car_by_Reg_num(CarRegNum)
        if cursor.rowcount > 0:
            query = 'UPDATE public."Cars"	SET  "CarType"='+"'"+str(CarType) +"'"+', "CarMakeID"='+"'"+str(CarMakeID) +"'"+ '	WHERE "CarRegNum" = '+ str(CarRegNum)+ ' ;'
            cursor.execute(query)
            self._connection.commit()
    
    
    def del_Car (self ,CarRegNum):
        cursor = self.get_cursor()
        record = get_Car_by_Reg_num(CarRegNum)
        if cursor.rowcount > 0:
            query = 'DELETE FROM public."Cars"	WHERE "CarRegNum"='+ str(CarRegNum)+ ';'
            cursor.execute(query)
            self._connection.commit()
        
        
        ##########Parking
        
        
    def get_parking_place_by_id (self,ParkingPlaceID):
        cursor = self.get_cursor()
        query = 'select * from public."ParkingPlace" where "ParkingPlaceID" ='+"'" + str(ParkingPlaceID)+"'"
        cursor.execute(query)
        self._connection.commit()
        record = cursor.fetchone()
        return record
    
    
    def create_parking_place (self,ParkingPlaceID,ParkingPlaceDesc=''):
        cursor = self.get_cursor()
        record = get_parking_place_by_id(ParkingPlaceID)
        if cursor.rowcount == 0:
            query = 'INSERT INTO public."ParkingPlace"("ParkingPlaceID", "ParkingPlaceDesc")' + "VALUES ('"+ str(ParkingPlaceID)+"','"+ str(ParkingPlaceDesc)+"');"
            cursor.execute(query)
            ParkingPlaceid=cursor.lastrowid
            self._connection.commit()
        else:
            ParkingPlaceid = record[0]
        return ParkingPlaceid
    
    def read_parking_place (self,):
        cursor = self.get_cursor()
        query = 'SELECT "ParkingPlaceID",  "ParkingPlaceDesc" FROM public."ParkingPlace";'
        cursor.execute(query)
        self._connection.commit()
        record = cursor.fetchall()
        return record
    
    def update_parking_place (self,ParkingPlaceID,ParkingPlaceDesc=''):
        cursor = self.get_cursor()
        record = get_parking_place_by_id(ParkingPlaceID)
        if cursor.rowcount > 0:
            query = 'UPDATE public."ParkingPlace"	SET ' +', "ParkingPlaceDesc"='+"'"+str(ParkingPlaceDesc) +"'"+ '	WHERE "ParkingPlaceID" = '+ str(ParkingPlaceID)+ ' ;'
            cursor.execute(query)
            self._connection.commit()
    
        
    def del_parking_place (self,ParkingPlaceID):
            cursor = self.get_cursor()
            record = get_parking_place_by_id(ParkingPlaceID)
            if cursor.rowcount > 0:
                query = 'DELETE FROM public."ParkingPlace"	WHERE "ParkingPlaceID"='+ str(ParkingPlaceID)+ ';'
                cursor.execute(query)
                self._connection.commit()
            
        
    ########Person
    
    
    def get_person_by_last_name (self,PersonLastName):
        cursor = self.get_cursor()
        query = 'SELECT * FROM public."Persons" WHERE "PersonLastName" ='+"'" + str(PersonLastName)+"'"
        cursor.execute(query)
        self._connection.commit()
        record = cursor.fetchone()
        return record
        
    
    
    def get_person_by_id (self,PersonID):
        cursor = self.get_cursor()
        query = 'select * from public."Persons" where "PersonID" ='+"'" + str(PersonID)+"'"
        cursor.execute(query)
        self._connection.commit()
        record = cursor.fetchone()
        return record

    def get_free_parking_place(self):
        cursor = self.get_cursor()
        query = 'select "ParkingPlaceID", "ParkingPlaceDesc" from public."ParkingPlace" where "ParkingPlaceID" not in (select "ParkingID" from public."Contract" where "ContractEnd" >= (SELECT CURRENT_DATE))'
        cursor.execute(query)
        self._connection.commit()
        record = cursor.fetchall()
        return record

        
    def chek_parking_place(self,id):
        cursor = self.get_cursor()
        query = 'select "ParkingPlaceID", "ParkingPlaceDesc" from public."ParkingPlace" where "ParkingPlaceID" not in (select "ParkingID" from public."Contract" where "ContractEnd" >= (SELECT CURRENT_DATE)) and "ParkingPlaceID" = '+ str(id)
        cursor.execute(query)
        self._connection.commit()
        record = cursor.fetchone()
        return record
    
    def create_person (self,PersonID, PersonLastName, PersonName,PersonMidleName):
        cursor = self.get_cursor()
        record = get_person_by_id(PersonID)
        if cursor.rowcount == 0:
            query = 'INSERT INTO public."Persons"("PersonID", "PersonLastName", "PersonName" , "PersonMidleName" )' + "VALUES ('"+ str(PersonID), str(PersonLastName), str(PersonName),str(PersonMidleName) +"');"
            cursor.execute(query)
        
            self._connection.commit()
        else:
            makeid = record[0]
        
    
    def read_person (self,):
        cursor = self.get_cursor()
        query = 'SELECT "PersonID", "PersonLastName", "PersonName","PersonMidleName" FROM public."Persons";'
        cursor.execute(query)
        self._connection.commit()
        record = cursor.fetchall()
        return record
        
    
    def update_person (self,PersonID, PersonLastName, PersonName,PersonMidleName):
        cursor = self.get_cursor()
        record = get_person_by_id(PersonID)
        if cursor.rowcount > 0:
            query = 'UPDATE public."Persons" SET "PersonLastName"='+"'"+str(PersonLastName) +"'"+'"PersonName"='+"'"+str(PersonName) +"'"+', "PersonMidleName"='+"'"+str(PersonMidleName) +"'"+ '	WHERE "PersonID" = '+ str(PersonID)+ ' ;'
            cursor.execute(query)
            self._connection.commit()
        
    
    
    def del_person (self,PersonID):
        cursor = self.get_cursor()
        record = get_person_by_id(PersonID)
        if cursor.rowcount > 0:
            query = 'DELETE FROM public."Persons"	WHERE "PersonID"='+ str(PersonID)+ ';'
            cursor.execute(query)
            self._connection.commit()
        
    
    #######Phones
    def get_phones_by_phones (self,Phone):
        cursor = self.get_cursor()
        query = 'select * from public."Phones" where "Phone" ='+"'" + str(Phone)+"'"
        cursor.execute(query)
        self._connection.commit()
        record = cursor.fetchone()
        return record
        
    
    
    
    def create_phones (self,PersonID,Phone):
        cursor = self.get_cursor()
        record = get_phones_by_phone(Phone)
        if cursor.rowcount == 0:
            query = 'INSERT INTO public."Phones"("PersonID", "Phone")' + "VALUES ('"+ str(PersonID)+"','"+ str(Phone)+"');"
            cursor.execute(query)
        
            self._connection.commit()
        else:
            makeid = record[0]
        return makeid
        
    
    def read_phones (self,):
        cursor = self.get_cursor()
        query = 'SELECT "PersonID", "Phone" FROM public."Phones";'
        cursor.execute(query)
        self._connection.commit()
        record = cursor.fetchall()
        return record
        
    
    def update_phones (self,PersonID,Phone):
        cursor = self.get_cursor()
        record = get_phones_by_phones(Phone)
        if cursor.rowcount > 0:
            query = 'UPDATE public."Phones"	SET , "PersonID"='+"'"+str(PersonID) +"'"+ '	WHERE "Phone" = '+ str(Phone)+ ' ;'
            cursor.execute(query)
            self._connection.commit()
        
    
    
    def del_phones (self,Phone):
        cursor = self.get_cursor()
        record = get_phones_by_phones(Phone)
        if cursor.rowcount > 0:
            query = 'DELETE FROM public."Phones"	WHERE "Phone"='+ str(Phone)+ ';'
            cursor.execute(query)
            self._connection.commit()
        
    
    ####### Contracts
    
    def get_contract_by_PersonID (self,PersonID):
        cursor = self.get_cursor()
        query = 'SELECT * FROM public."Contract" WHERE "PersonID" ='+"'" + str(PersonID)+"'"
        cursor.execute(query)
        self._connection.commit()
        record = cursor.fetchone()
        return record
        
    def get_currentContract_by_carRegNum(self,CarNumber):
        cursor = self.get_cursor()
        query = '''select "ContractID", "CarNumber", "ParkingID", "Contract"."PersonID" as "PersonID", "ContractStart", "ContractEnd","CarMakeID","CarType", "CarTypeName", "MakeName", "PersonLastName", "PersonName", "PersonMidleName"
                    from public."Contract" 
	                    INNER JOIN public."Cars" on public."Contract"."CarNumber" = public."Cars"."CarRegNum" 
	                    INNER JOIN public."CarType" on public."Cars"."CarType" = public."CarType"."CarTypeID"
	                    INNER JOIN public."Makes" on public."Makes"."MakeID" = public."Cars"."CarMakeID"
	                    INNER JOIN public."Persons" on public."Persons"."PersonID" = public."Contract"."PersonID"
	                where "ContractID"=(select max("ContractID") from public."Contract" where "CarNumber" = \'''' + str(CarNumber)+"')"
        cursor.execute(query)
        self._connection.commit()
        record = cursor.fetchone()
        return record
    
    def get_contract_by_ParkingID (self,ParkingID):
        cursor = self.get_cursor()
        query = 'select * from public."Contract" where "ParkingID" ='+"'" + str(ParkingID)+"'"
        cursor.execute(query)
        self._connection.commit()
        record = cursor.fetchone()
        return record
       
    def close_contract(self,id):
        cursor = self.get_cursor()
        query = 'UPDATE public."Contract"	SET  "ContractEnd"= (SELECT CURRENT_DATE-1)  WHERE "ContractID" = '+ str(ContractID)+ ' ;'
        cursor.execute(query)
        self._connection.commit()
    
    def get_contract_by_ContractID (self,ContractID):
        cursor = self.get_cursor()
        query = 'select * from public."Contract" where "ContractID" ='+"'" + str(ContractID)+"'"
        cursor.execute(query)
        self._connection.commit()
        record = cursor.fetchone()
        return record
    
    
    def clear_data(self):
        cursor = self.get_cursor()
        query = ''' select '' as  "ContractID", '' as "CarNumber", '' as "ParkingID", '' as "PersonID", '' as "ContractStart", '' as "ContractEnd", '' as "CarMakeID", '' as "CarType", '' as "CarTypeName", '' as "MakeName", '' as "PersonLastName", '' as "PersonName", '' as "PersonMidleName"'''
        cursor.execute(query)
        self._connection.commit()
        record = cursor.fetchone()
        return record
        
    
    def create_contract (self,CarNumber,PersonID,ParkingID,ContractEnd):
        cursor = self.get_cursor()
        query = 'INSERT INTO public."Contract"("CarNumber","PersonID","ParkingID","ContractStart","ContractEnd")' + "VALUES ('"+ str(CarNumber)+"',"+str(PersonID)+","+str(ParkingID)+","+"(SELECT CURRENT_DATE) " +","+"(SELECT CURRENT_DATE +"+str(days)+"));"
        cursor.execute(query)
    
        self._connection.commit()
        
    
    def read_contract (self,):
        cursor = self.get_cursor()
        query = '''select "ContractID", "CarNumber", "ParkingID", "Contract"."PersonID" as "PersonID", "ContractStart", "ContractEnd","CarMakeID","CarType", "CarTypeName", "MakeName", "PersonLastName", "PersonName", "PersonMidleName"
                    from public."Contract" 
	                INNER JOIN public."Cars" on public."Contract"."CarNumber" = public."Cars"."CarRegNum" 
	                INNER JOIN public."CarType" on public."Cars"."CarType" = public."CarType"."CarTypeID"
	                INNER JOIN public."Makes" on public."Makes"."MakeID" = public."Cars"."CarMakeID"
	                INNER JOIN public."Persons" on public."Persons"."PersonID" = public."Contract"."PersonID"'''
        cursor.execute(query)
        self._connection.commit()
        record = cursor.fetchall()
        return record
        
    
    def update_contract (self,ContractID,CarNumber,PersonID,ParkingID,ContractStart,ContractEnd):
        cursor = self.get_cursor()
        record = get_contract_by_ContractID(ContractID)
        if cursor.rowcount > 0:
            query = 'UPDATE public."Contract"	SET  "CarNumber"='+"'"+str(CarNumber) +"'"+', "PersonID"='+"'"+str(PersonID) +"'"+', "ParkingID"='+"'"+str(ParkingID)+"'"+ ', "ContractStart"='+"'"+str(ContractStart) +"'"+ ', "ContractEnd"='+"'"+str(ContractEnd) +"'"+'	WHERE "ContractID" = '+ str(ContractID)+ ' ;'
            cursor.execute(query)
            self._connection.commit()
        
    
   

    def del_contract_by_temp_table_CarNum(self,CarNum):
        cursor = self.get_cursor()
        query ='''DROP TABLE IF EXISTS public."TMP_Contract";
    CREATE TABLE IF NOT EXISTS public."TMP_Contract"("ContractID" smallint NOT NULL,"CarNumber" character varying(8) COLLATE pg_catalog."default" NOT NULL,"PersonID" bigint NOT NULL,"ParkingID" smallint NOT NULL,"ContractStart" date NOT NULL,"ContractEnd" date NOT NULL);
   insert into public."TMP_Contract" ("ContractID","PersonID","CarNumber","ParkingID","ContractStart","ContractEnd") select "ContractID","PersonID","CarNumber","ParkingID","ContractStart","ContractEnd" from public."Contract" where "CarNumber" =  /' '''+ str(CarNum)+ ''' /'' ;
    delete from public."Contract" where "ContractID" in (select distinct "ContractID" from public."TMP_Contract" );
    delete from public."Cars" where "CarRegNum" =  /' '''+ str(CarNum)+ ''' /';
    delete from public."Persons" where "PersonID" in (select distinct "PersonID" from public."TMP_Contract" ) and "PersonID" not in (select distinct "PersonID" from public."Contract" where "PersonID"  in (select distinct "PersonID" from public."TMP_Contract" ) );
    DROP TABLE public."TMP_Contract";'''

        cursor.execute(query)
        self._connection.commit()

    def del_contract_by_temp_table_personID(self,personID):
        self._connection= self.get_connection()
        cursor = self.get_cursor()
        query ='''DROP TABLE IF EXISTS public."TMP_Contract";
    CREATE TABLE IF NOT EXISTS public."TMP_Contract"("ContractID" bigint NOT NULL,"CarNumber" character varying(8) COLLATE pg_catalog."default" NOT NULL,"PersonID" bigint NOT NULL,"ParkingID" smallint NOT NULL,"ContractStart" date NOT NULL,"ContractEnd" date NOT NULL);
   insert into public."TMP_Contract" ("ContractID","PersonID","CarNumber","ParkingID","ContractStart","ContractEnd") select "ContractID","PersonID","CarNumber","ParkingID","ContractStart","ContractEnd" from public."Contract" where "PersonID"= ''' +str(personID)+  ''';
    delete from public."Contract" where "ContractID" in (select distinct "ContractID" from public."TMP_Contract" );
    delete from public."Cars" where "CarRegNum" in (select distinct "CarRegNum" from public."TMP_Contract" ) and "CarRegNum" not in (select distinct "CarRegNum" from public."Contract" where "CarRegNum"  in (select distinct "CarRegNum" from public."TMP_Contract" ) );
   delete from public."Persons" where "PersonID" =  ''' +str(personID)+  ''';
    DROP TABLE public."TMP_Contract";'''
        cursor.execute(query)
        self._connection.commit()

    def del_contract_by_temp_table_ContractID(self,ContractID):
        self._connection= self.get_connection()
        cursor = self.get_cursor()
        query ='''DROP TABLE IF EXISTS public."TMP_Contract";
    CREATE TABLE IF NOT EXISTS public."TMP_Contract"
    (
    "ContractID" smallint NOT NULL,
    "CarNumber" character varying(8) COLLATE pg_catalog."default" NOT NULL,
    "PersonID" bigint NOT NULL,
    "ParkingID" smallint NOT NULL,
    "ContractStart" date NOT NULL,
    "ContractEnd" date NOT NULL
    );
    insert into public."TMP_Contract" ("ContractID","PersonID","CarNumber","ParkingID","ContractStart","ContractEnd") select "ContractID","PersonID","CarNumber","ParkingID","ContractStart","ContractEnd" from public."Contract" where "ContractID"='''+str(ContractID)  +''';
    delete from public."Contract" where "ContractID" in (select distinct "ContractID" from public."TMP_Contract" );
    delete from public."Cars" where "CarRegNum" in (select distinct "CarRegNum" from public."TMP_Contract" ) and "CarRegNum" not in (select distinct "CarRegNum" from public."Contract" where "CarRegNum" in (select distinct "CarRegNum" from public."TMP_Contract" ) );
    delete from public."Persons" where "PersonID" in (select distinct "PersonID" from public."TMP_Contract" ) and "PersonID" not in (select distinct "PersonID" from public."Contract" where "PersonID"  in (select distinct "PersonID" from public."TMP_Contract" ) );
    DROP TABLE public."TMP_Contract";'''

        cursor.execute(query)
        self._connection.commit()

    def random_create (self, param):
        cursor = self.get_cursor()
        query = "CALL public.generate_data("+str(param)+");"
        cursor.execute(query)
        self._connection.commit()
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

    def select(self,parking_start , parking_end ,PersonPart, Date ):
        cursor = self.get_cursor()
        query = '''select "ContractID", "CarNumber", "ParkingID", "Contract"."PersonID" as "PersonID", "ContractStart", "ContractEnd","CarMakeID","CarType", "CarTypeName", "MakeName", "PersonLastName", "PersonName", "PersonMidleName"
	    from public."Contract"
        INNER JOIN public."Cars" on public."Contract"."CarNumber" = public."Cars"."CarRegNum" 
        INNER JOIN public."CarType" on public."Cars"."CarType" = public."CarType"."CarTypeID"
        INNER JOIN public."Makes" on public."Makes"."MakeID" = public."Cars"."CarMakeID"
        INNER JOIN public."Persons" on public."Persons"."PersonID" = public."Contract"."PersonID"
        where "ContractID" > 1
        and "ParkingID" between '''+parking_start +''' and '''+ parking_end +'''
        and "PersonLastName" like  '''+"'%"+ PersonPart +"%'"+'''
        and "ContractEnd" >  '''+"'"+ Date +"'"

        cursor.execute(query)
        self._connection.commit()
        record = cursor.fetchone()
        return record
