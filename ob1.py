'''
    Function: learn how to define class in Python (object-oriented)
'''


class OldStyle:
    def __init__(self, name, description):
        self.name = name
        self.description = description


class NewStyle(object):
    def __init__(self, name, description):
        self.name = name
        self.description = description





if __name__ == '__main__':
    old = OldStyle('old', 'Old Style Class')
    print(old)
    print(type(old))
    print(dir(old))   # dir() --> print the attributes of class
    print('---------')
    new = NewStyle('new', 'New Style Class')
    print(new)
    print(type(new))
    print(dir(new))
    print('---------')