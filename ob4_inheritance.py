class Programmer(object):
    hobby = 'computer game'

    def __init__(self, name, age, weight):
        self.name = name  # public attribute
        self._age = age  # private attribute
        self.__weight = weight  # protected attribute

    @classmethod
    def get_hobby(cls):
        return cls.hobby

    @property
    def get_weight(self):
        return self.__weight

    def self_introduction(self):  # class method
        print('My name is %s \nI am %s years old\n' % (self.name, self._age))


class BackendProgrammer(Programmer):

    def __init__(self, name, age, weight, language):
        super(BackendProgrammer, self).__init__(name, age, weight)
        self.language = language


if __name__ == '__main__':
    # programmer = Programmer('Jia Hu', 28, 58)
    # print(dir(programmer))
    # print(programmer.__dict__)
    # print(programmer.get_hobby())
    # print(programmer.get_weight)
    # programmer.self_introduction()

    programmer = BackendProgrammer("Jia Hu", 27, 58, 'Python')
    print(dir(programmer))
    print(programmer.__dict__)
    print(type(programmer))
    print(isinstance(programmer, Programmer))
