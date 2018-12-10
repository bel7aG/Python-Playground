from Person import Person

class Developer(Person):
    __is_developer = None

    def __init__(self, name, surname, age, language, is_developer):
        super(Developer, self).__init__(name, surname, age, language)
        self.__is_developer = is_developer

    def set_is_developer(self, is_developer):
        self.__is_developer = is_developer

    def get_is_developer(self):
        return self.__is_developer

    def get_type(self):
        print('Developer Class')


    def toString(self):
        return '{} {} is {} Developer \n\n\t\tage: {}.'.format(self.get_name(), self.get_surname(), self.get_language(), self.get_age())
