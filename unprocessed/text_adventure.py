from game.maps import Map
from game.inventory import Inventory
from game.objects import Objects
from game.player import Player

class TextAdventureGame:
    def __init__(self, map_data, inventory_data, objects_data):
        self.map = Map(map_data["rooms"])
        self.inventory = Inventory(inventory_data["items"])
        self.objects = Objects(objects_data["objects"])
        self.player = None

    def create_player(self):
        name = input("Enter your name: ")
        starting_room_name = input("Enter the starting room: ")
        starting_room = self.map.get_room(starting_room_name)
        self.player = Player(name, starting_room)

    def move_player(self, direction):
        self.player.move(direction)

    def take_item(self, item):
        self.player.take_item(item)

    def use_item(self, item):
        self.player.use_item(item)

    def play(self):
        self.create_player()

        while True:
            print("\n---")
            print("Current Room:", self.player.current_room["name"])
            print("Description:", self.player.current_room["description"])

            command = input("Enter your command: ").lower()

            if command == "move":
                direction = input("Enter the direction to move: ")
                self.move_player(direction)
            elif command == "take":
                item = input("Enter the item to take: ")
                self.take_item(item)
            elif command == "use":
                item = input("Enter the item to use: ")
                self.use_item(item)
            elif command == "quit":
                break
            else:
                print("Invalid command.")
