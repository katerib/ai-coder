from game.maps import Map
from game.objects import Objects
from game.player import Player
import os


class TextAdventureGame:
    MIN_WIDTH = 80          # Minimum terminal width in columns
    MIN_HEIGHT = 24         # Minimum terminal height in lines

    def __init__(self, map_data, objects_data):
        # def __init__(self, objects_data):
        self.map = Map(map_data["maps"])
        self.objects = Objects(objects_data["objects"])
        self.player = None

    @staticmethod
    def print_valid_commands():
        """
        Static method to print a list of supported verbs (commands) for the player to utilize.
        """
        print("Valid Commands:")
        print("- move (to navigate between rooms)")
        print("- take (to pick up items)")
        print("- use (to use items)")
        print("- quit (to exit the game)")
        # Add more commands as needed

    @staticmethod
    def check_terminal_size():
        """
        Static method to check the terminal size. If the terminal size is too small, the game will not be playable.
        Terminal size should be checked throughout gameplay, likely before each command is entered.
        """
        size = os.get_terminal_size()
        if size.lines < TextAdventureGame.MIN_HEIGHT or size.columns < TextAdventureGame.MIN_WIDTH:
            print(
                f"Your terminal window size is {size.lines} lines by {size.columns} columns.")
            print(
                f"This game requires a minimum size of {TextAdventureGame.MIN_HEIGHT} lines by {TextAdventureGame.MIN_WIDTH} columns.")
            print("Please resize your terminal and start the game again.\n")
            exit()

    def create_player(self):
        name = input("Enter your name: ")
        starting_room = self.map.get_room("Room_1")
        self.player = Player(name, starting_room, self.map, self.objects)

    def move_player(self, direction):
        self.player.move(direction)

    def take_item(self, item):
        item_data = self.player.take_item_from_room(item)
        if item_data:
            self.player.inventory.add_item(item_data, quantity=1)
            print(f"You picked up {item_data}")
        else:
            print("There is no such item in this room.")

    def use_item(self, item):
        item_data = self.player.inventory.get_item(item)
        if item_data:
            # Implement the logic for using the item
            print(f"You used {item_data['name']}")
        else:
            print("You don't have that item in your inventory.")

    def play(self):
        self.check_terminal_size()
        self.create_player()

        # Print valid commands at the start of the game
        self.print_valid_commands()

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
