import json
from text_adventure import TextAdventureGame

# Load data from JSON files
with open("map_data.json") as file:
    map_data = json.load(file)

with open("inventory_data.json") as file:
    inventory_data = json.load(file)

with open("objects_data.json") as file:
    objects_data = json.load(file)

# Create an instance of the game and start playing
game = TextAdventureGame(map_data, inventory_data, objects_data)
game.play()
