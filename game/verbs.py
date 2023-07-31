# verbs.py
def hit_verb(map, target):
    """
    Handle the "hit" verb action.
    """
    if target in map['feature_item'] and map['action_verb'] == 'hit':
        print(map['feature_item'][target])
    else:
        print(f"You can't hit that.")

def pull_verb(map, object_to_pull):
    """
    Handle the "pull" verb action.
    """
    if object_to_pull in map['feature_item'] and map['action_verb'] == 'pull':
        print(map['feature_item'][object_to_pull])
    else:
        print(f"You can't pull that.")

def read_verb(map, object_to_read):
    """
    Handle the "read" verb action.
    """
    if object_to_read in map['feature_item'] and map['action_verb'] == 'read':
        print(map['feature_item'][object_to_read])
    else:
        print(f"There is nothing to read.")

def look_verb(room):
    """
    Handle the "look" verb action. Repeats the long form explanation of the room
    """
    print(f"{room['description']} \n\n")
    for _, item_location in room['interactive_items'].items():
        print(f"{item_location} ", end="")
    print(room['feature_location_description'])

def glance_verb(room, inventory, objects, obj):
    """
    Similar to the "look at" verb action, but gives a shorter description of the feature or object.
    """
    print("You glance around the room.")
    item_description = objects.get_description(obj)

    if any(item.lower() == obj.lower() for item in inventory.items):
        if item_description:
            print(f"You're holding {item_description}")
        else:
            print(f"You look at the {obj} but find nothing of interest.")
    elif any(item.lower() == obj.lower() for item in room["interactive_items"]):
        if item_description:
            print(f"You see {item_description}")
        else:
            print(f"You look at the {obj} but find nothing of interest.")

    else:
        print("You can't look at that.")


def look_at_verb(room, inventory, objects, obj):
    """
    Handle the "look at" verb action. Gives a fictionally interesting explanation of the feature or object.
    """
    print(f"You look at the {obj}.")
    item_description = objects.get_interaction(obj)


    if any(item.lower() == obj.lower() for item in inventory.items):
        obj_in_inventory = next((item for item in inventory.items if item.lower() == obj.lower()), None)
        if obj_in_inventory:
            print(f"You found the {obj_in_inventory} in your inventory.")
            if item_description:
                print(f"{item_description}")
            else:
                print(f"You look at the {obj_in_inventory} but find nothing of interest.")
        else:
            print(f"You don't see the {obj} here or in your inventory.")
    elif any(item.lower() == obj.lower() for item in room["interactive_items"]):
        if item_description:
            print(item_description)
        else:
            print(f"You look at the {obj} but find nothing of interest.")
    else:
        print(f"You don't see the {obj} here or in your inventory.")


def inventory_verb(inventory):
    """
    Handle the "inventory" verb action.
    """
    if len(inventory.view_inventory()) == 0:
        print("It looks like you don't have anything in your inventory.")
    else:
        print("Inventory:")
        for item in inventory.view_inventory().keys():
            print(f"- {item}: 1")
