class Person:
    __name = None
    __surname = None
    __age = 0
    __language = None

    def __init__(self, name, surname, age, language):
        self.__name = name
        self.__surname = surname
        self.__age = age
        self.__language = language

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name


    def set_surname(self, surname):
        self.__surname = surname

    def get_surname(self):
        return self.__surname


    def set_age(self, age):
        self.__age = age

    def get_age(self):
        return self.__age

    def set_language(self, language):
        self.__language = language

    def get_language(self):
        return self.__language

    def get_type(self):
        print('Person Class')
