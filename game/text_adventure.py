from game.maps import Map
from game.objects import Objects
from game.player import Player
from game.command_parser import CommandParser
from game.verbs import hit_verb, pull_verb, look_verb, look_at_verb, inventory_verb, glance_verb, read_verb
import os
import json


class TextAdventureGame:
    MIN_WIDTH = 80
    MIN_HEIGHT = 24

    SAVE_FILE = "backup/save_data.json"

    def __init__(self):
        self.map = Map()
        self.objects = Objects()
        self.create_player()

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
        print("- read (to read something)")
        print("- look (to look around the room)")
        print("- look at (to look at something)")
        print("- inventory (to view your inventory)")
        print("- quit or exit (to exit the game)")
        print("- save (to save the game)")
        print("- load (to load the game)")
        print("- reset backups (to delete all saved data)")

        print("Not all commands are shown here. Try to think of other commands that might work! \n")

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

    def save_game(self):
        """
        Method to save the game state to a JSON file with the fixed filename "save_data.json".
        """
        game_state = {
            "player": self.player.serialize(),
            "map": self.map.serialize(),
            "objects": self.objects.serialize(),
            "visited_rooms": list(self.player.visited_rooms)
        }

        for room in self.map.map_data.values():
            items_to_remove = []
            for item in room["interactive_items"]:
                if item.lower() in self.player.inventory.items:
                    items_to_remove.append(item)
            for item in items_to_remove:
                del room["interactive_items"][item]

        backup_directory = os.path.dirname(TextAdventureGame.SAVE_FILE)
        os.makedirs(backup_directory, exist_ok=True)

        with open(TextAdventureGame.SAVE_FILE, "w") as file:
            json.dump(game_state, file)

    def load_game(self):
        """
        Method to load the game state from the JSON file with the fixed filename "save_data.json".
        """
        if os.path.exists(TextAdventureGame.SAVE_FILE):
            with open(TextAdventureGame.SAVE_FILE, "r") as file:
                game_state = json.load(file)

            self.map.deserialize(game_state["map"])
            self.objects.deserialize(game_state["objects"])
            self.player = Player.deserialize(
                game_state["player"], self.map, self.objects)

            # Restore visited rooms if it exists in the saved data
            if "visited_rooms" in game_state:
                self.player.visited_rooms = set(game_state["visited_rooms"])

            # Remove items from the interactive_items of each room if they are in the player's inventory
            for room in self.map.map_data.values():
                items_to_remove = []
                for item in room["interactive_items"]:
                    if item.lower() in self.player.inventory.items:
                        items_to_remove.append(item)
                for item in items_to_remove:
                    del room["interactive_items"][item]

            return True
        else:
            return False

    def reset_game(self, exit_game=False):
        """
        Method to reset the game state.
        """
        self.map = Map()
        self.objects = Objects()
        self.create_player()

        if exit_game:
            print("Game has been reset and will now exit.")
            exit()
        else:
            print("Game has been reset.")

    def reset_backups(self, exit_after_reset=False):
        """
        Method to delete the saved_data.json file.
        """
        if os.path.exists(TextAdventureGame.SAVE_FILE):
            os.remove(TextAdventureGame.SAVE_FILE)
            print("All saved data has been deleted.")
            self.reset_game(exit_after_reset)
        else:
            print("No saved data found to delete.")

    def create_player(self):
        """
        Method to create a new player.
        """
        name = input("Enter your name: ")
        starting_room = self.map.get_current_room()
        self.player = Player(name, starting_room, self.map, self.objects)

    def move_player(self, direction):
        """
        Method to move the player in a given direction. The direction should be a string. Supports moving "back". 
        """
        direction = direction.strip()
        if direction == "back":
            self.player.move_back()
        else:
            previous_room = self.player.current_room
            self.player.move(direction)

    def take_item(self, item):
        item_name, item_location = self.player.take_item_from_room(item)
        if item_name:
            self.player.inventory.add_item(item_name.lower(), item_location)
            print(f"You picked up {item_name}")
        else:
            print("There is no such item in this room or you can't pick this item up.")

    def use_item(self, item):
        """
        Method to use an item from the player's inventory. The item should be a string.
        """
        inventory_item = self.player.inventory.get_item(item)

        if inventory_item:
            
            item_data = self.objects.get_object(item)

            if item_data:

                if item_data["equipped"]:
                    print(f"The {item} is already equipped.")
                else:
                    self.objects.mark_item_as_equipped(item)
                    print(item_data["effect"])
            else:
                print("Item not found.")
        else:
            print("You don't have that item in your inventory.")

    def handle_command(self, verb, obj):
        if verb == "move" or verb == 'go':
            self.move_player(obj)
        elif verb == "take" or verb == "pick up" or verb == "grab":
            self.take_item(obj)
        elif verb == "use" or verb == "examine" or verb == "show" or \
                verb == "turn on" or verb == "turn off" or verb == "insert" or verb == "upgrade" \
                or verb == "cut" or verb == "activate" or verb == "deactivate" or verb == "display" or \
                verb == "study" or verb == "decipher" or verb == "upgrade":
            self.use_item(obj)
        elif verb == "quit" or verb == "exit":
            exit()
        elif verb == "hit" or verb == "strike" or verb == "push" or verb == "open":
            hit_verb(self.player.current_room, obj)
        elif verb == "pull" or verb == "tug" or verb == "yank":
            pull_verb(self.player.current_room, obj, self.player.inventory)
        elif verb == "read" or verb == "analyze":
            read_verb(self.player.current_room, obj)
        elif verb == "look":
            look_verb(self.player.current_room)
        elif verb == "glance":
            glance_verb(self.player.current_room,
                        self.player.inventory, self.objects, obj)
        elif verb == "glance at":
            glance_verb(self.player.current_room,
                        self.player.inventory, self.objects, obj)
        elif verb == "look at":
            look_at_verb(self.player.current_room,
                         self.player.inventory, self.objects, obj)
        elif verb == "inventory":
            inventory_verb(self.player.inventory)
        elif verb == "help":
            self.help_command()
        elif verb == "drop":
            self.player.drop_item(obj)
        elif verb == "save":
            self.save_game()
            print(f"Game saved to {TextAdventureGame.SAVE_FILE} successfully.")
        elif verb == "load":
            check = self.load_game()
            if check:
                print(f"Game loaded successfully.")
            else:
                print("No saved game data found.")
        elif verb == "reset backups" or verb == "reset" or verb == "reset backup":
            self.reset_backups()
        elif verb == "back":
            self.move_player("back")
        else:
            print("Invalid command.")

    def play(self):
        self.check_terminal_size()

        print(
            f"\nWelcome to the game {self.player.get_name()}! Type help for a list of commands. \nNot sure what to do first? Get started by looking around the room with 'look'.")

        while True:
            self.check_terminal_size()

            print("\nWhat will you do next?")

            command = input("Enter your command: ").lower()

            verb, obj = CommandParser.parse_command(command, self.map)
            print("\n")

            if not verb:
                print("Invalid command.")
            else:
                self.handle_command(verb, obj)
