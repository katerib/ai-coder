import json
import os.path

class Map:
    def __init__(self):
        self.json_file_name = "data/maps.json"
        self.json_file_name = os.path.normpath(self.json_file_name)

        with open(self.json_file_name, 'r') as data:
            self.map_data = json.load(data)

        self.room_list = []
        for room in self.map_data['maps']:
            print(self.map_data['maps'][room])
            self.room_list.append(self.map_data['maps'][room])
        print(len(self.room_list))
        self.room_count = 0

        # Set up detail variables and initialize first map room
        self.current_room = self.room_list[0].copy()


    def get_current_room(self):
        return self.current_room

    def is_move_valid(self, direction):
        """checks the current room valid moves"""
        try:
            if self.current_room['valid_moves'][direction]:
                return True
            else:
                return False
        except:
            print("Wrong direction input")
            return False

    def get_next_room(self):
        """moves linear to next room if right direction chosen"""
        if self.room_count == 9:
            print("Game is over")
            return False

        self.room_count += 1
        return self.room_list[self.room_count]

    def get_room(self, roomname):
        print(self.current_room)
        return self.map_data['maps'][roomname]

    def get_last_room(self):
        return self.last_room

    def get_valid_travel_directions(self):
        return self.current_room['valid_moves']

    def add_object(self, object_to_add):
        """Adds object to self.map_data and current room data"""
        try:
            self.current_room['object_interaction'][object_to_add]['obtained'] = True
            return True
        except KeyError:
            return False

    def is_object_obtained(self, object_to_check):
        """Checks if an object has been obtained"""
        try:
            return self.current_room['object_interaction'][object_to_check]['obtained']
        except KeyError:
            return False
