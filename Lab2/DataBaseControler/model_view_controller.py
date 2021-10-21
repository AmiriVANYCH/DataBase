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


class View(object):

    @staticmethod
    def show_bullet_point_list(item_type, items):
        print('--- {} LIST ---'.format(item_type.upper()))
        for item in items:
            print('* {}'.format(item))

    @staticmethod
    def show_number_point_list(item_type, items):
        print('--- {} LIST ---'.format(item_type.upper()))
        for i, item in enumerate(items):
            print('{}. {}'.format(i+1, item))

    @staticmethod
    def show_items( items):
        print('//////////////////////////////////////////////////////////////')
        for item in items:
            print(item)
        print('//////////////////////////////////////////////////////////////')

    @staticmethod
    def display_missing_item_error(item, err):
        print('**************************************************************')
        print('We are sorry, we have no {}!'.format(item.upper()))
        print('{}'.format(err.args[0]))
        print('**************************************************************')

    @staticmethod
    def display_item_already_stored_error(item, item_type, err):
        print('**************************************************************')
        print('Hey! We already have {} in our {} list!'
              .format(item.upper(), item_type))
        print('{}'.format(err.args[0]))
        print('**************************************************************')

    @staticmethod
    def display_item_not_yet_stored_error(item, item_type, err):
        print('**************************************************************')
        print('We don\'t have any {} in our {} list. Please insert it first!'
              .format(item.upper(), item_type))
        print('{}'.format(err.args[0]))
        print('**************************************************************')

    @staticmethod
    def display_item_stored(item, item_type):
        print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
        print('Hooray! We have just added some {} to our {} list!'
              .format(item.upper(), item_type))
        print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')

    @staticmethod
    def display_change_item_type(older, newer):
        print('---   ---   ---   ---   ---   ---   ---   ---   ---   ---   --')
        print('Change item type from "{}" to "{}"'.format(older, newer))
        print('---   ---   ---   ---   ---   ---   ---   ---   ---   ---   --')

    @staticmethod
    def display_item_updated(item, o_price, o_quantity, n_price, n_quantity):
        print('---   ---   ---   ---   ---   ---   ---   ---   ---   ---   --')
        print('Change {} price: {} --> {}'
              .format(item, o_price, n_price))
        print('Change {} quantity: {} --> {}'
              .format(item, o_quantity, n_quantity))
        print('---   ---   ---   ---   ---   ---   ---   ---   ---   ---   --')

    @staticmethod
    def display_item_deletion(name):
        print('--------------------------------------------------------------')
        print('We have just removed {} from our list'.format(name))
        print('--------------------------------------------------------------')
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
