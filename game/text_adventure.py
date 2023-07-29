from game.maps import Map
from game.objects import Objects
from game.player import Player
from game.command_parser import CommandParser
from game.verbs import hit_verb, pull_verb, look_verb, look_at_verb, inventory_verb, glance_verb, read_verb
import os


class TextAdventureGame:
    MIN_WIDTH = 80          # Minimum terminal width in columns
    MIN_HEIGHT = 24         # Minimum terminal height in lines

    def __init__(self):
        self.map = Map()
        self.objects = Objects()
        self.player = None

    @staticmethod
    def help_command():
        """
        Static method to print a list of supported verbs (commands) for the player to utilize.
        """
        print("Valid Commands:")
        print("- move (to navigate between rooms)")
        print("- take (to pick up items)")
        print("- use (to use items)")
        print("- hit (to hit something)")
        print("- pull (to pull something)")
        print("- go (to navigate between rooms)")
        print("- eat (to eat something)")
        print("- look (to look around the room)")
        print("- look at (to look at something)")
        print("- inventory (to view your inventory)")
        print("- quit (to exit the game)")


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
        starting_room = self.map.get_current_room()
        self.player = Player(name, starting_room, self.map, self.objects)

    def move_player(self, direction):
        self.player.move(direction.strip())

    def take_item(self, item):
        item_data = self.player.take_item_from_room(item)
        if item_data:
            self.player.inventory.add_item(item_data, quantity=1)
            self.player.current_room["isPresent"] = False            
            print(f"You picked up {item_data}")
        else:
            print("There is no such item in this room.")

    def use_item(self, item):
        # Get the item data from the Objects class based on the item name
        item_data = self.objects.get_object(item)

        if item_data:
            item_name = item_data["name"]

            # Check if the item exists in the player's inventory
            inventory_item = self.player.inventory.get_item(item)
            if inventory_item:
                if item_data["equipped"]:
                    # Item is already equipped, print a message to inform the player
                    print(f"The {item_name} is already equipped.")
                else:
                    # Mark the item as equipped in the objects JSON
                    self.objects.mark_item_as_equipped(item)
                    # Print out the effect of using the item
                    self.objects.handle_item_effect(item_data)
            else:
                print("You don't have that item in your inventory.")
        else:
            print("Item not found.")

    def handle_command(self, verb, obj):
        if verb == "move":
            self.move_player(obj)
        elif verb == "take":
            self.take_item(obj)
        elif verb == "use":
            self.use_item(obj)
        elif verb == "quit" or verb == "exit":
            exit()
        elif verb == "hit":
            hit_verb(obj)
        elif verb == "pull":
            pull_verb(obj)
        elif verb == "go":
            self.move_player(obj)
        elif verb == "read":
            read_verb(obj)
        elif verb == "look":
            look_verb(self.player.current_room)
        elif verb == "glance":
            glance_verb(self.player.current_room, self.player.inventory, self.objects, obj)
        elif verb == "glance at":
            glance_verb(self.player.current_room, self.player.inventory, self.objects, obj)
        elif verb == "look at":
            look_at_verb(self.player.current_room, self.player.inventory, self.objects, obj)
        elif verb == "inventory":
            inventory_verb(self.player.inventory)
        elif verb == "help":
            self.help_command()
        elif verb == "drop":
            self.player.drop_item(obj)
        else:
            print("Invalid command.")

    def play(self):
        # commented out for testing
        # self.check_terminal_size()
        self.create_player()

        # # Print valid commands at the start of the game
        print(f"\nWelcome to the game {self.player.get_name()}! Type help for a list of commands. \nNot sure what to do first? Get started by looking around the room with 'look'.")

        while True:
            # print("Current Room:", self.player.current_room["name"])
            # print("Description:", self.player.current_room["description"])
            print("\nWhat will you do next?")

            command = input("Enter your command: ").lower()

            verb, obj = CommandParser.parse_command(command)
            # print(f"VERB: {verb}, OBJ: {obj}")
            print("\n")

            if not verb:
                print("Invalid command.")
            else:
                self.handle_command(verb, obj)

