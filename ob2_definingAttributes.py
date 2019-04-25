class Programmer(object):
    hobby = 'computer game'

    def __init__(self, name, age, weight):
        self.name = name  # public attribute
        self._age = age  # private attribute
        self.__weight = weight  # protected attribute

    def get_weight(self):
        return self.__weight



if __name__ == '__main__':
    programmer = Programmer('Jia Hu', 25, 58)
    print(dir(programmer))
    print(programmer.__dict__)
    print(programmer.get_weight())
    print(programmer._Programmer__weight)  # change the attribute, make it public
