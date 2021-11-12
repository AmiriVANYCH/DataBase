import basic_backend
import mvc_exceptions as mvc_exc





class View(object):

    @staticmethod
    def query(str):
        print(str)
    def show_FIO(self,LName,Name,MName):
        print("Введено:")
        print(LName +" "+ Name +" "+ MName)
        print("Підтвердити \n  0 - ні    1 - так ")
    def print_name_query(self):
        print("Введіть імя")

    def print_error_name_query(self):
        print("Не правильне значення")

    def print_code_query(self):
        print("Введіть код користувача")

    def print_error_code_query(self):
        print("Введено неправильний код")

    def print_car_num_query(self):
        print("Введено нномер машини")

    def print_error_car_num_query(self):
        print("Введено неправильний код")

    def print_parking_place_query(self):
        print("введіть номер паркомісцяякий хочете вибрати")

    def print_parking_place_error(self):
        print("Місце зайняте, введіть інше або 0 для відміни")

    def print_day_querty(self):
        print("Введіть кількість днів на яку відкриваєте контракт")

    def print_make_type(self):
        print("Введіть марку автомобіля")


    def print_make_type_error(self):
        print("Виробника не знайдено")

    def print_car_type(self):
        print("Введіть тип автомобіля")
    def print_car_type_error(self):
        print("Вибрано не правильний тип авто")

    def print_person_info(self):
        print("Введіть код користувача")

    def print_person_error(self):
        print("Введене не правильне значення")

    def print_person_masseg(self,user):
        print("Знайдений користувач")
        print(user)

    def print_person_masseg_LName(self):
        print("Введіть фамілію")

    def print_person_masseg_Name(self):
        print("Введіть імя")

    def print_person_masseg_MName(self):
        print("Введіть по-батькові, якщо є")


    def get_int(self):
        int = input()
        if int.isdigit():
            return int
        else:
            return
    def print_contract(self,contract):
        print("Знайдено контракт за цим номером.")
        print(contract)
        print("Ви можете змінити тільки паркомісце\n 0 - ні    1 - так ")

    def print_table(self,rows,cols):
        lenth = len(rows)
        row_num = lenth // cols
        if lenth % cols != 0:
            row_num +=1
        for i in range(0,row_num):
            for j in range (0,cols):
                if i+j*row_num < lenth:
                    print(rows[i+j*row_num], end='')
                    print("   ", end='')
            print('')



    def get_main_menu_sel(self):
        start = '''Початкове меню
        
        1 - Додати договір
        2 - Курувати виробниками авто
        3 - Керувати типами авто
        4 - Керувати власниками авто
        5 - Керувати авто
        4 - Пошук


        
        '''
        start = start.split("\n")
        print("****************************************")
        for line in start:
            print("*"+" "*5+line+" "*(33-len(line)) +"*")
        print("****************************************")
        cose = input()
        return cose
    def search_menu ():
        start = '''
        1 - Знайти договір за номером телефону
        2 - Знайти вільні місця
        3 - Знайти договір за власником авто
        4 - Знайти договір за номером авто
        5 - Знайти договір за періодом підписання
        6 - Знайти договір за періодом завершення10 - Знайти договір за кількістю активних днів
        7 - Знайти договір за вільними параметрами'''
        start = start.split("\n")
        print("****************************************")
        for line in start:
            print("*"+" "*5+line+" "*(33-len(line)) +"*")
        print("****************************************")
        cose = input()
        return cose
    def get_make_menu(self):
        start = '''Меню марок
        
        1 - Додати марку
        2 - Видалити марку
        3 - Редагувати марку
        '''
        start = start.split("\n")
        print("****************************************")
        for line in start:
            print("*"+" "*5+line+" "*(33-len(line)) +"*")
        print("****************************************")
        cose = input()
        return cose

    def get_type_menu(self):
        start = '''Меню типів авто
        
        1 - Додати тип авто
        2 - Видалити тип авто
        3 - Редагувати тип авто
        '''
        start = start.split("\n")
        print("****************************************")
        for line in start:
            print("*"+" "*5+line+" "*(33-len(line)) +"*")
        print("****************************************")
        cose = input()
        return cose

    def get_str(self):
        str = input()
        return str
    def get_free_parking_place(self,parking_place):
        self.view.show_items(items)

    def print_make_control_del_masseg(self):
        print("Введіть айді марки яку хочете видалити")

    def print_car_type_control_del_masseg(self):
        print("Введіть айді типу авто який хочете видалити")

    @staticmethod
    def show_items( items):
        print('//////////////////////////////////////////////////////////////')
        for item in items:
            print(item)
        print('//////////////////////////////////////////////////////////////')

    def print_make_control_MakeType(self):
        print("Введіть назву марки ")
    def print_make_control_MakeDiscription(self):
        print("Введіть опис марки якщо потрібно")


    def print_carType_control_CarTypeID(self):
        print("Введіть ідентифікатор типу авто")
    def print_carType_control_CarTypeName(self):
        print("Введіть назву типу авто")

    def print_make_control_MakeID(self):
        print("Введіть айді марки яку хочете змінити")

    def print_car_type_control_del_masseg(self):
        print("Введіть айді типу авто який хочете видалити")
