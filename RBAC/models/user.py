class User():
    def __init__(self, name:str, roles:list):
        self.__name = name
        self.__roles = roles

    @property
    def name(self):
        return self.__name

    @property
    def roles(self):
        return self.__roles