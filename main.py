import json
from game.text_adventure import TextAdventureGame

# Load data from JSON files
with open("data/objects_data.json") as file:
    objects_data = json.load(file)
    # print(objects_data["objects"]["cast"]["name"])


# Create an instance of the game and start playing
game = TextAdventureGame(objects_data)
game.play()
