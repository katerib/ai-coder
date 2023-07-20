import json
import os.path

class Map:
    def __init__(self):
        self.json_file_name = "maps_data/maps.json"
        self.json_file_name = os.path.normpath(self.json_file_name)

        with open(self.json_file_name, 'r') as data:
            self.map_data = json.load(data)

        # Set up detail variables and initialize first map room
        self.current_room = None
        self.start_room()

    def start_room(self):
        """Initializes first room where the game starts"""
        self.current_room = self.map_data['maps']['Room_1']

    def get_current_room(self):
        return self.current_room

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
