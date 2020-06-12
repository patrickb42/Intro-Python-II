# Implement a class to hold room information. This should have name and
# description attributes.
from pyrsistent import pvector
class Room:
    def __init__(self, name: str, description: str, items=None):
        self.__name = name
        self.__description = description
        self.items = pvector(items if items is not None else [])
        self.n_to: 'Room' = None
        self.s_to: 'Room' = None
        self.e_to: 'Room' = None
        self.w_to: 'Room' = None

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

    def __str__(self):
        return f"""Room: {self.name}
{self.description}
Items: {self.items}"""

    def __repr__(self):
        return f"Room(name='{self.name}', description='{self.description}'"
