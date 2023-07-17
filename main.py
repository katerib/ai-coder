import json
from text_adventure import TextAdventureGame

# Load data from JSON files
with open("data/objects_data.json") as file:
    objects_data = json.load(file)
    # print(objects_data["objects"]["cast"]["name"])

with open("unprocessed/data/map_data.json") as file:
    map_data = json.load(file)


# Create an instance of the game and start playing
game = TextAdventureGame(map_data, objects_data)
game.play()
