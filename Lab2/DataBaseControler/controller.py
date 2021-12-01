import basic_backend
import mvc_exceptions as mvc_exc
import datetime

class Controller(object):

    data = None

    def __init__(self, model, view):
        self.model = model
        self.view = view

    def query(self,str):
        self.view.query(str)

    def fill_day_info(self):
        self.view.print_day_querty()
        self.data["days"] = self.view.get_int()

    def clear_data(self):
        self.data = self.model.clear_data()


    def fill_contract(self):
        Carnum= self.get_car_num()
        self.data = self.get_currentContract_by_carRegNum(Carnum)
        if self.data:
            self.view.print_contract(self.data)
            cose = self.view.get_int()
            if cose == "0":
                return
            elif cose == "1":

                self.fill_parking_info()
                self.fill_day_info()
                self.create_contract()
        else:
            
            self.clear_data()
            self.data["CarNumber"] = Carnum
            self.fill_avto()
            self.fill_parking_info()
            self.fill_person_info()
            self.fill_day_info()
            self.create_contract()

    def run(self):
        cose = self.view.get_main_menu_sel()
        if cose == "1":
            self.fill_contract()
            
        if cose == "2":
            self.make_control()
        
        if cose == "3":
            self.CarType_control()

        if cose == "4":
            self.del_contract()
        if cose == "5":
            self.random_create()
        if cose == "6":
            self.select_contract()

    def make_control(self):
        self.clear_data()
        cose = self.view.get_make_menu()
        if cose == "1":
            self.view.print_make_control_MakeType()
            self.data["MakeName"] = self.view.get_str()
            self.view.print_make_control_MakeDiscription()
            self.data["MakeDescription"] = self.view.get_str()
            self.save_make()
        if cose == "2":
            self.show_make()
            self.view.print_make_control_del_masseg()
            cose = self.view.get_str()
            if self.get_make_by_id(cose):
                self.del_make(cose)
                return
        if cose == "3":
            self.show_make()
            self.view.print_make_control_MakeID()
            self.data["MakeID"] = self.view.get_str()
            self.view.print_make_control_MakeType()
            self.data["MakeName"] = self.view.get_str()
            self.view.print_make_control_MakeDiscription()
            self.data["MakeDescription"] = self.view.get_str()
            self.save_make(True)

    def random_create(self):
        self.model.random_create(self.view.random_create_mess())
    

    def CarType_control(self):  
        self.clear_data()
        cose = self.view.get_type_menu()
        if cose == "1":
            self.view.print_carType_control_CarTypeName()
            self.data["CarTypeName"] = self.view.get_str()
            self.save_carType()
        if cose == "2":
            self.show_CarType()
            self.view.print_car_type_control_del_masseg()
            cose = self.view.get_int()
            if self.get_CarType_by_id(cose):
                self.del_CarType(cose)
                return
        if cose == "3":
            self.show_CarType()
            self.view.print_carType_control_CarTypeID()
            self.data["CarTypeID"] = self.view.get_str()
            self.view.print_carType_control_CarTypeName()
            self.data["CarTypeName"] = self.view.get_str()
            self.save_carType(True)




    def fill_person_info(self):
        self.data["PersonID"] = self.get_person_code()
        resalt = self.get_person_by_id(self.data["PersonID"])
        if resalt:
            self.view.print_person_masseg(resalt)
            self.data["PersonID"] = resalt["PersonID"]
            self.data["PersonLastName"] = resalt["PersonLastName"]
            self.data["PersonMidleName"] = resalt["PersonMidleName"]
            self.data["PersonName"] = resalt["PersonName"]
        else:
            self.view.print_person_masseg_LName()
            self.data["PersonLastName"] = self.Get_Name()
            self.view.print_person_masseg_Name()
            self.data["PersonName"] = self.Get_Name()
            self.view.print_person_masseg_MName()
            self.data["PersonMidleName"] = self.Get_Name()
        self.view.show_FIO(self.data["PersonLastName"],self.data["PersonName"], self.data["PersonMidleName"])



    def fill_make(self):
        self.show_make()
        self.view.print_make_type()
        self.data["CarMake"] = self.view.get_int()
        while self.data["CarMake"] != "0"  and not self.get_make_by_id(self.data["CarMake"]):
            self.view.print_make_type_error()
            self.data["CarMake"] = self.view.get_int()
        if self.data["CarMake"] == "0":
            return -1
        return 1

    def fill_car_type(self):
        self.show_CarType()
        self.view.print_car_type()
        self.data["CarType"] = self.view.get_int()
        while self.data["CarType"] != "0" and not self.get_CarType_by_id(self.data["CarType"]):
            self.view.print_car_type_error()
            self.data["CarType"] = self.view.get_int()
        if self.data["CarType"] == "0":
            return -1
        return 1

    def fill_avto(self):
        self.fill_make()
        self.fill_car_type()




    def Get_Name(self):
        chars = "йцукенгшщзхїфівапролджєячсмитьбю"
        charMas = "ЙЦУКЕНГШЩЗХЇФІВАПРОЛДЖЄЯЧСМИТЬБЮ"
        name = self.view.get_str()
        if name:
            if name[0] not in charMas:
                self.view.print_error_name_query()
                return

            if name :
                for char in name[1:len(name)-1]:
                    if char.isalpha() or (char in chars) :
                        continue
                    else:
                       self.view.print_error_name_query()
                       item = Get_Name()
                       return item 
            else:
                print_error_name_query()
                item = Get_Name()
                return item
        return name


    def fill_parking_info(self):
        #self.show_parking_place()
        self.view.print_parking_place_query()
        ParkingID = self.view.get_int()
        if 'ParkingID' in self.data:
            while self.chek_parking_place(ParkingID):
                self.view.print_parking_place_error()
                ParkingID = input()
                if ParkingID == "0":
                    return -1
        self.data["ParkingID"] = ParkingID
        return 1



    def get_person_code(self):
        self.view.print_code_query()
        code = self.view.get_int()
        if len(code) == 11:
            return code
        else:
            self.view.print_error_code_query()
            return

    def get_car_num(self):
        self.view.print_car_num_query()
        chars= "QWERTYUIOPASDFGHJKLZXCVBNM1234567890"
        num= self.view.get_str()
        for char in num:
            if char in chars:
                continue
            else:
                self.view.print_error_car_num_query()
                return
        if len(num) == 8:
            return num
        else:
            self.view.print_error_car_num_query()
            return
    

    def save_car(self,update=False):
        if update:
            self.update_Car(self.data["CarNumber"],self.data["CarMake"],self.data["CarType"])
            return
        if self.data["CarMake"] != '':
            if not self.get_Car_by_Reg_num(self.data["CarNumber"]):
                self.create_Car(self.data["CarNumber"],self.data["CarMake"],self.data["CarType"])
                return

    def save_make(self,update=False):
        if update:
            self.update_make(self.data["MakeID"],self.data["MakeName"],self.data["MakeDescription"])
            return
        if self.data["MakeName"] != '':
            if not self.get_make_by_name(self.data["MakeName"]):
                self.create_make(self.data["MakeName"],self.data["MakeDescription"])
                return

    def save_carType(self,update=False):
        if update:
            self.update_CarType(self.data["CarTypeID"],self.data["CarTypeName"])
            return
        if self.data["CarTypeName"] !="":
                self.create_CarType(self.data["CarTypeName"])
                return


    def show_make(self):
        items = self.model.read_make()
        self.view.show_items(items)

    def get_make_by_name(self, Makes_name):
            item = self.model.get_make_by_name(Makes_name)
            return item
    def get_make_by_id(self, MakesID):
            item = self.model.get_make_by_id(MakesID)
            return item

    def create_make(self, MakeName,MakeDescription):
        self.model.create_make(MakeName,MakeDescription)

    def update_make(self,MakeID,MakeName,MakeDescription):
        self.model.update_make (MakeID,MakeName,MakeDescription)

    def del_make(self, MakeID):
        self.model.del_make (MakeID)


    def show_CarType(self):
        items = self.model.read_CarType()
        self.view.show_items(items)
    
    
    def get_CarType_by_id (self,CarTypeID):

        items = self.model.get_CarType_by_id(CarTypeID)
        return items
        
    
    
    def create_CarType (self,CarTypeName):
        items = self.model.create_CarType (CarTypeName)

        
    

        
    def update_CarType(self,CarTypeID,CarTypeName):
        self.model.update_CarType(CarTypeID,CarTypeName)
    
    
    def del_CarType (self , CarTypeID):
        self.model.del_CarType (CarTypeID)


########Cars
    
    def get_Car_by_Reg_num (self,CarRegNum):
         items = self.model.get_Car_by_Reg_num (CarRegNum)
         return items

    def create_Car (self,CarRegNum,CarMakeID,CarType):
         items = self.model.create_Car (CarRegNum,CarMakeID,CarType)
         self.view.show_items(items)
        
    
    def show_Car (self,):
         items = self.model.read_Car ()
         self.view.show_items(items)
        
    
    def update_Car (self,CarRegNum,CarMakeID,CarType):
        self.model.update_Car (CarRegNum,CarMakeID,CarType)
        
    
    
    def del_Car (self,CarRegNum):
        self.model.del_Car (CarRegNum)
        
    
    
    ##########Parking
    
    
    def get_parking_place_by_id (self,ParkingPlaceID):
         items = self.model.get_parking_place_by_id (ParkingPlaceID)
         self.view.show_items(items)
      

    def chek_parking_place(self,id):
        items = self.model.chek_parking_place (id)
        if items:
            return False
        else:
            return True
    
    def create_parking_place (self,ParkingPlaceID,ParkingPlaceDesc):
         items = self.model.create_parking_place (ParkingPlaceID,ParkingPlaceDesc)
         self.view.show_items(items)
        
    
    def show_parking_place (self,):
         items = self.model.read_parking_place ()
         self.view.print_parking_info(items)
        
    
    def update_parking_place (self,ParkingPlaceID,ParkingPlaceDesc):
        self.model.update_parking_place (ParkingPlaceID,ParkingPlaceDesc)
        
    
    
    def del_parking_place (self,ParkingPlaceID):
        self.model.del_parking_place (ParkingPlaceID)
        
    
    ########Person
    def save_person(self,update = False):
        if update:
            self.update_person(self.data["PersonID"], self.data["PersonLastName"], self.data["PersonName"],self.data["PersonMidleName"] )
            return 
        if self.data["PersonLastName"] != '':
            if not self.get_person_by_id(self.data["PersonID"]):
                self.create_person(self.data["PersonID"], self.data["PersonLastName"], self.data["PersonName"],self.data["PersonMidleName"] )
                return
    
    def get_person_by_last_name (self,PersonLastName):
         items = self.model.get_person_by_last_name (PersonLastName)
         self.view.show_items(items)
        
    
    
    def get_person_by_id (self,PersonID):
         items = self.model.get_person_by_id (PersonID)
         return items
        
    
    
    def create_person (self,PersonID, PersonLastName, PersonName,PersonMidleName):
         items = self.model.create_person (PersonID, PersonLastName, PersonName,PersonMidleName)
         self.view.show_items(items)
        
    
    def show_person (self,):
         items = self.model.read_person ()
         self.view.show_items(items)
        
    
    def update_person (self,PersonID, PersonLastName, PersonName,PersonMidleName):
        self.model.update_person (PersonID, PersonLastName, PersonName,PersonMidleName)
        
    
    
    def del_person (self,PersonID):
        self.model.del_person (PersonID)
        
    
    #######Phones
    def get_phones_by_phones (self,Phone):
         items = self.model.get_phones_by_phones (Phone)
         self.view.show_items(items)
        
    
    
    
    def create_phones (self,PersonID,Phone):
         items = self.model.create_phones (PersonID,Phone)

        
    
    def show_phones (self,):
        self.model. read_phones ()
        
    
    def update_phones (self,PersonID,Phone):
        self.model.update_phones (PersonID,Phone)
        
    
    
    def del_phones (self,Phone):
        self.model.del_phones (Phone)
        
    
    ####### Contracts
    
    def get_contract_by_PersonID (self,PersonID):
         items = self.model.get_contract_by_PersonID (PersonID)
         self.view.show_items(items)
        
    def get_currentContract_by_carRegNum(self,CarNumber):
        items = self.model.get_currentContract_by_carRegNum (CarNumber)
        return items
    
    def get_contract_by_ParkingID (self,ParkingID):
         items = self.model.get_contract_by_ParkingID (ParkingID)
         self.view.show_items(items)
       
    
    
    def get_contract_by_ContractID (self,ContractID):
         items = self.model.get_contract_by_ContractID (ContractID)
         self.view.show_items(items)
        
    def close_contract(self,id):
        self.model.close_contract(id)
    
    def create_contract (self):
        self.save_car()
        self.save_person()
        self.model.create_contract (self.data["CarNumber"],self.data["PersonID"],self.data["ParkingID"],self.data["days"])
        
    
    def show_contract (self,):
         items = self.model.read_contract ()
         self.view.show_items(items)
        
    
    def update_contract (self,ContractID,CarNumber,PersonID,ParkingID,ContractStart,ContractEnd):
        self.model.update_contract (ContractID,CarNumber,PersonID,ParkingID,ContractStart,ContractEnd)
        
    
    


    def del_contract(self):
        cose= self.view.del_masseg()
        if cose == "1":
            resald= self.view.del_masseg_contract_id()
            self.model.del_contract_by_temp_table_ContractID(resald)
        elif cose == "2":
            resald= self.view.del_masseg_regnum()
            self.model.del_contract_by_temp_table_CarNum(resald)
        elif cose == "3":
            resald= self.view.del_masseg_person_id()            
            self.model.del_contract_by_temp_table_personID(resald)
######
    def select_contract(self):
        parking_start=self.view.get_str()
        parking_end=self.view.get_str()
        PersonPart= self.view.get_str()
        Date= self.view.get_str()
        contract= self.model.select(parking_start , parking_end ,PersonPart, Date )
        if contract:
            self.view.show_item(contract)

