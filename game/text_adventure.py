from game.maps import Map
from game.objects import Objects
from game.player import Player
import os

class TextAdventureGame:
    MIN_WIDTH = 80          # Minimum terminal width in columns
    MIN_HEIGHT = 24         # Minimum terminal height in lines

    def __init__(self, map_data, objects_data):
        self.map = Map(map_data["rooms"])
        self.objects = Objects(objects_data["objects"])
        self.player = None

    @staticmethod
    def check_terminal_size():
        """
        Static method to check the terminal size. If the terminal size is too small, the game will not be playable.
        Terminal size should be checked throughout gameplay, likely before each command is entered.
        """
        size = os.get_terminal_size()
        if size.lines < TextAdventureGame.MIN_HEIGHT or size.columns < TextAdventureGame.MIN_WIDTH:
            print(f"Your terminal window size is {size.lines} lines by {size.columns} columns.")
            print(f"This game requires a minimum size of {TextAdventureGame.MIN_HEIGHT} lines by {TextAdventureGame.MIN_WIDTH} columns.")
            print("Please resize your terminal and start the game again.\n")
            exit()

    def create_player(self):
        name = input("Enter your name: ")
        starting_room_name = input("Enter the starting room: ")
        starting_room = self.map.get_room(starting_room_name)
        self.player = Player(name, starting_room, self.map, self.objects)

    def move_player(self, direction):
        self.player.move(direction)

    def take_item(self, item):
        self.player.take_item(item)

    def use_item(self, item):
        self.player.use_item(item)

    def play(self):
        self.check_terminal_size()
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
