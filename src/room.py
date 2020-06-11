# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
    n_to: 'Room'
    s_to: 'Room'
    e_to: 'Room'
    w_to: 'Room'

    def __init__(self, name: str, description: str):
        self.__name = name
        self.__description = description

    @property
    def name(self):
        '''returns name'''
        return self.__name
    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def description(self):
        '''returns description'''
        return self.__description
