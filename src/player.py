# Write a class to hold player information, e.g. what room they are in
# currently.
from room import Room
class Player:
    def __init__(self, name: str, current_room: Room):
        self.__name = name
        self.__current_room = current_room
    
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
                print()
                print(self.current_room)
            return True
