from Person import Person

class Programmer(Person):
    __is_programmer = None

    def __init__(self, name, surname, age, language, is_programmer):
        super(Programmer, self).__init__(name, surname, age, language)
        self.__is_programmer = is_programmer

    def set_is_programmer(self, is_programmer):
        self.__is_programmer = is_programmer

    def get_is_programmer(self):
        return self.__is_programmer

    def get_type(self):
        print('Programmer Class')

    def toString():
        return '{} {} is {} Programmer \n\n\t\tage: {}'.format(self.__name,
                                                                self.__surname,
                                                                self.__language,
                                                                self.__age)
