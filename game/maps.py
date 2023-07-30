import json


class Map:
    def __init__(self):
        with open("data/maps.json", 'r') as file:
            data = json.load(file)

        self.map_data = data["maps"]
        self.room_count = 0
        self.current_room = self.map_data[list(self.map_data.keys())[0]]

    def get_current_room(self):
        return self.current_room

    def is_move_valid(self, direction):
        """checks the current room valid moves"""
        try:
            valid_moves = self.current_room['valid_moves']
            # Checks if the direction is in the valid moves dictionary and check if it is true
            if direction in valid_moves and valid_moves[direction]:
                return True
            else:
                return False
        except KeyError:
            print("Wrong direction input")
            return False

    def set_current_room(self, room):
        """Sets the current room"""
        self.current_room = room

    def get_next_room(self):
        """moves linear to next room if right direction chosen"""
        room_keys = list(self.map_data.keys())
        if self.room_count >= len(room_keys) - 1:
            return False

        self.room_count += 1
        next_room_key = room_keys[self.room_count]
        return self.map_data[next_room_key]

    def get_room_names(self):
        """Returns a list of room names"""
        return [self.map_data[room_key]["name"].lower() for room_key in self.map_data]

