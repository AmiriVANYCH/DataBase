import basic_backend
import mvc_exceptions as mvc_exc

class Controller(object):

    def __init__(self, model, view):
        self.model = model
        self.view = view

    def show_make(self):
        items = self.model.read_make()
        self.view.show_items(items)

    def get_make_by_name(self, Makes_name):
        #try:
            item = self.model.get_make_by_name(Makes_name)
            #self.view.show_item(item_type, item_name, item)
        #except mvc_exc.ItemNotStored as e:
            #self.view.display_missing_item_error(item_name, e)

    def create_make(self, MakeName,MakeDescription):

        #try:
        self.model.create_make(MakeName,MakeDescription)
            #self.view.display_item_stored(name, item_type)
        #except mvc_exc.ItemAlreadyStored as e:
            #self.view.display_item_already_stored_error(name, item_type, e)

    def update_make(self,MakeID,MakeName,MakeDescription):

        #try:
        self.model.update_make (MakeID,MakeName,MakeDescription)
            #self.view.display_item_updated(name, older['price'], older['quantity'], price, quantity)
        #except mvc_exc.ItemNotStored as e:
            #self.view.display_item_not_yet_stored_error(name, item_type, e)
            # if the item is not yet stored and we performed an update, we have
            # 2 options: do nothing or call insert_item to add it.
            # self.insert_item(name, price, quantity)

    def del_make(self, MakeID):
        #try:
        self.model.del_make (MakeID)
            #self.view.display_item_deletion(name)
        #except mvc_exc.ItemNotStored as e:
            #self.view.display_item_not_yet_stored_error(name, item_type, e)

###Type

    def get_CarType_by_name (self,CarTypeName):
        return self.model.get_CarType_by_name (CarTypeName)
    
    
    def get_CarType_by_id (self,CarTypeID):

        return self.model.get_CarType_by_id (CarTypeID)
        
    
    
    def create_CarType (self,CarTypeName):
        return self.model.create_CarType (CarTypeName)
        
    
    def read_CarType (self):
        return self.model.read_CarType ()
        
    def update_CarType(self,CarTypeID,CarTypeName):
        self.model.update_CarType(CarTypeID,CarTypeName)
    
    
    def del_CarType (self , CarTypeID):
        self.model.del_CarType (CarTypeID)


########Cars
    
    def get_Car_by_Reg_num (self,CarRegNum):
        self.model.get_Car_by_Reg_num (CarRegNum)
        
    
    
    
    
    def create_Car (self,CarRegNum,CarMakeID,CarType):
        self.model.create_Car (CarRegNum,CarMakeID,CarType)
        
    
    def read_Car (self,):
        self.model.read_Car ()
        
    
    def update_Car (self,CarRegNum,CarMakeID,CarType):
        self.model.update_Car (CarRegNum,CarMakeID,CarType)
        
    
    
    def del_Car (self,CarRegNum):
        self.model.del_Car (CarRegNum)
        
    
    
    ##########Parking
    
    
    def get_parking_place_by_id (self,ParkingPlaceID):
        self.model.get_parking_place_by_id (ParkingPlaceID)
        
    
    
    def create_parking_place (self,ParkingPlaceID,ParkingPlaceDesc):
        self.model.create_parking_place (ParkingPlaceID,ParkingPlaceDesc)
        
    
    def read_parking_place (self,):
        self.model.read_parking_place ()
        
    
    def update_parking_place (self,ParkingPlaceID,ParkingPlaceDesc):
        self.model.update_parking_place (ParkingPlaceID,ParkingPlaceDesc)
        
    
    
    def del_parking_place (self,ParkingPlaceID):
        self.model.del_parking_place (ParkingPlaceID)
        
    
    ########Person
    
    
    def get_person_by_last_name (self,PersonLastName):
        self.model.get_person_by_last_name (PersonLastName)
        
    
    
    def get_person_by_id (self,PersonID):
        self.model.get_person_by_id (PersonID)
        
    
    
    def create_person (self,PersonID, PersonLastName, PersonName,PersonMidleName):
        self.model.create_person (PersonID, PersonLastName, PersonName,PersonMidleName)
        
    
    def read_person (self,):
        self.model.read_person ()
        
    
    def update_person (self,PersonID, PersonLastName, PersonName,PersonMidleName):
        self.model.update_person (PersonID, PersonLastName, PersonName,PersonMidleName)
        
    
    
    def del_person (self,PersonID):
        self.model.del_person (PersonID)
        
    
    #######Phones
    def get_phones_by_phones (self,Phone):
        self.model.get_phones_by_phones (Phone)
        
    
    
    
    def create_phones (self,PersonID,Phone):
        self.model.create_phones (PersonID,Phone)
        
    
    def read_phones (self,):
        self.model. read_phones ()
        
    
    def update_phones (self,PersonID,Phone):
        self.model.update_phones (PersonID,Phone)
        
    
    
    def del_phones (self,Phone):
        self.model.del_phones (Phone)
        
    
    ####### Contracts
    
    def get_contract_by_PersonID (self,PersonID):
        self.model.get_contract_by_PersonID (PersonID)
        
    
    
    def get_contract_by_ParkingID (self,ParkingID):
        self.model.get_contract_by_ParkingID (ParkingID)
       
    
    
    def get_contract_by_ContractID (self,ContractID):
        self.model.get_contract_by_ContractID (ContractID)
        
    
    
    def create_contract (self,CarNumber,PersonID,ParkingID,ContractStart,ContractEnd):
        self.model.create_contract (CarNumber,PersonID,ParkingID,ContractStart,ContractEnd)
        
    
    def read_contract (self,):
        self.model.read_contract (self,)
        
    
    def update_contract (self,ContractID,CarNumber,PersonID,ParkingID,ContractStart,ContractEnd):
        self.model.update_contract (ContractID,CarNumber,PersonID,ParkingID,ContractStart,ContractEnd)
        
    
    
    def del_contract (self,ContractID):
        self.model.del_contract (ContractID)

######
