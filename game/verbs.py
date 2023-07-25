# verbs.py
def hit_verb(target):
    """
    Handle the "hit" verb action.
    """
    print(f"You hit {target}.")

def pull_verb(object_to_pull):
    """
    Handle the "pull" verb action.
    """
    print(f"You pull the {object_to_pull}.")

def eat_verb(item_to_eat):
    """
    Handle the "eat" verb action.
    """
    print(f"You eat the {item_to_eat}.")

def look_verb(room_description):
    """
    Handle the "look" verb action.
    """
    print(room_description)

def look_at_verb(obj):
    """
    Handle the "look at" verb action.
    """
    if obj in self.player.current_room["interactive_items"]:
        item_description = self.player.current_room["object_interaction"].get(obj)
        if item_description:
            print(item_description["description"])
        else:
            print(f"You look at the {obj} but find nothing of interest.")
    elif obj in self.player.inventory.items:
        item_data = self.player.inventory.get_item(obj)
        print(item_data["description"])
    else:
        print("You can't look at that.")

def inventory_verb(inventory):
    """
    Handle the "inventory" verb action.
    """
    print("Inventory:")
    for item, quantity in inventory.view_inventory().items():
        print(f"- {item}: {quantity}")
