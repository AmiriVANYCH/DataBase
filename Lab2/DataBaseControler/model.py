import basic_backend
import mvc_exceptions as mvc_exc


class ModelBasic(object):



    def get_make_by_name (self,MakeName):
        return basic_backend.get_make_by_name (MakeName)
    
    
    def get_make_by_id (self,MakeID):
        return basic_backend.get_make_by_id (MakeID)
        
    
    
    def create_make (self,MakeName,MakeDescription):
        return basic_backend.create_make (MakeName,MakeDescription)
        
    
    def read_make (self):
        return basic_backend.read_make ()
        
    def update_make(self,MakeID,MakeName,MakeDescription):
        basic_backend.update_make(MakeID,MakeName,MakeDescription)
    
    
    def del_make (self , MakeID):
        basic_backend.del_make (MakeID)

##############Type


    def get_CarType_by_name (self,CarTypeName):
        return basic_backend.get_CarType_by_name (CarTypeName)
    
    
    def get_CarType_by_id (self,CarTypeID):
        return basic_backend.get_CarType_by_id (CarTypeID)
        
    
    
    def create_CarType (self,CarTypeName):
        return basic_backend.create_CarType (CarTypeName)
        
    
    def read_CarType (self):
        return basic_backend.read_CarType ()
        
    def update_CarType(self,CarTypeID,CarTypeName):
        basic_backend.update_CarType(CarTypeID,CarTypeName)
    
    
    def del_CarType (self , CarTypeID):
        basic_backend.del_CarType (CarTypeID)


    ########Cars
    
    def get_Car_by_Reg_num (self,CarRegNum):
        return basic_backend.get_Car_by_Reg_num (CarRegNum)
        
    
    
    
    
    def create_Car (self,CarRegNum,CarMakeID,CarType):
        return basic_backend.create_Car (CarRegNum,CarMakeID,CarType)
        
    
    def read_Car (self,):
        return basic_backend.read_Car ()
        
    
    def update_Car (self,CarRegNum,CarMakeID,CarType):
        basic_backend.update_Car (CarRegNum,CarMakeID,CarType)
        
    
    
    def del_Car (self,CarRegNum):
        basic_backend.del_Car (CarRegNum)
        
    
    
    ##########Parking
    
    
    def get_parking_place_by_id (self,ParkingPlaceID):
        return basic_backend.get_parking_place_by_id (ParkingPlaceID)
        
    
    
    def create_parking_place (self,ParkingPlaceID,ParkingPlaceDesc):
        return basic_backend.create_parking_place (ParkingPlaceID,ParkingPlaceDesc)
        
    
    def read_parking_place (self,):
        return basic_backend.read_parking_place ()
        
    
    def update_parking_place (self,ParkingPlaceID,ParkingPlaceDesc):
        basic_backend.update_parking_place (ParkingPlaceID,ParkingPlaceDesc)
        
    
    
    def del_parking_place (self,ParkingPlaceID):
        basic_backend.del_parking_place (ParkingPlaceID)
        
    
    ########Person
    
    
    def get_person_by_last_name (self,PersonLastName):
        return basic_backend.get_person_by_last_name (PersonLastName)
        
    
    
    def get_person_by_id (self,PersonID):
        return basic_backend.get_person_by_id (PersonID)
        
    
    
    def create_person (self,PersonID, PersonLastName, PersonName,PersonMidleName):
        return basic_backend.create_person (PersonID, PersonLastName, PersonName,PersonMidleName)
        
    
    def read_person (self,):
        return basic_backend.read_person ()
        
    
    def update_person (self,PersonID, PersonLastName, PersonName,PersonMidleName):
        basic_backend.update_person (PersonID, PersonLastName, PersonName,PersonMidleName)
        
    
    
    def del_person (self,PersonID):
        basic_backend.del_person (PersonID)
        
    
    #######Phones
    def get_phones_by_phones (self,Phone):
        return basic_backend.get_phones_by_phones (Phone)
        
    
    
    
    def create_phones (self,PersonID,Phone):
        return basic_backend.create_phones (PersonID,Phone)
        
    
    def read_phones (self,):
        return basic_backend. read_phones ()
        
    
    def update_phones (self,PersonID,Phone):
        basic_backend.update_phones (PersonID,Phone)
        
    
    
    def del_phones (self,Phone):
        basic_backend.del_phones (Phone)
        
    
    ####### Contracts
    
    def get_contract_by_PersonID (self,PersonID):
        return basic_backend.get_contract_by_PersonID (PersonID)
        
    
    
    def get_contract_by_ParkingID (self,ParkingID):
        return basic_backend.get_contract_by_ParkingID (ParkingID)
       
    
    
    def get_contract_by_ContractID (self,ContractID):
        return basic_backend.get_contract_by_ContractID (ContractID)
        
    
    
    def create_contract (self,CarNumber,PersonID,ParkingID,ContractStart,ContractEnd):
        return basic_backend.create_contract (CarNumber,PersonID,ParkingID,ContractStart,ContractEnd)
        
    
    def read_contract (self,):
        return basic_backend.read_contract (self,)
        
    
    def update_contract (self,ContractID,CarNumber,PersonID,ParkingID,ContractStart,ContractEnd):
        basic_backend.update_contract (ContractID,CarNumber,PersonID,ParkingID,ContractStart,ContractEnd)
        
    
    
    def del_contract (self,ContractID):
        basic_backend.del_contract (ContractID)

######
