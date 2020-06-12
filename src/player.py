# Write a class to hold player information, e.g. what room they are in
# currently.
from pyrsistent import pvector, typing
from typing import List
from room import Room
from item import Item

class Player:
    def __init__(self, name: str, current_room: Room, items=None):
        self.__name = name
        self.__current_room = current_room
        # self.__items: List[Item] = items if items is not None else []
        self.__items = pvector(items) if items is not None else pvector()

    @property
    def name(self):
        return self.__name

    @property
    def current_room(self) -> Room:
        return self.__current_room

    @current_room.setter
    def current_room(self, new_room):
        if self.__current_room.n_to is new_room\
        or self.__current_room.s_to is new_room\
        or self.__current_room.e_to is new_room\
        or self.__current_room.w_to is new_room:
            self.__current_room = new_room
        else:
            raise Exception(f'room {repr(new_room)} is not connected \
to the current room {repr(self.__current_room)}')

    def move_to(self, direction: str, print_room=True):
        new_room: Room = getattr(self.current_room, f'{direction}_to')
        if new_room is None:
            print("There's no room in that direction")
            return False
        else:
            self.current_room = new_room
            if print_room:
                print(self.current_room)
            return True

    @property
    def items(self):
        return self.__items

    @items.setter
    def items(self, items):
        self.__items = items

    # not sure if I should make item source a string or Item object
    def take_item(self, item: str, src=None):
        if src is not None:
            try:
                src.drop_item(item)
            except Exception:
                print(f'error dropping having src {src} drop item {item}')
        self.items = self.items.append(item)

    def drop_item(self, item, dest=None):
        self.items = self.items.delete(item)
        if dest is not None:
            dest.take_item(item)
