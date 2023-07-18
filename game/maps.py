class Map:
    def __init__(self, data):
        self.rooms = data

    def get_room(self, room_name):
        return self.rooms[room_name]
