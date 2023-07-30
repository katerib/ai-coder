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
    if room["isPresent"] == True:
        print(f"{room['description']} \n\n{room['obj_description']}")
    else:
        print(room['description'])

def glance_verb(room, inventory, objects, obj):
    """
    Similar to the "look at" verb action, but gives a shorter description of the feature or object. 
    """
    print("You glance around the room.")
    item_description = objects.get_description(obj)

    if obj in room["interactive_items"]:
        if item_description:
            print(f"You see {item_description}")
        else:
            print(f"You look at the {obj} but find nothing of interest.")
    elif obj in inventory.items:  # Corrected this line
        print(f"You found the {obj} in your inventory.")
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
    print("You look around.")
    item_description = objects.get_interaction(obj)
    if obj in room["interactive_items"]:
        if item_description:
            print(item_description)
        else:
            print(f"You look at the {obj} but find nothing of interest.")
    elif obj in inventory.items:  # Corrected this line
        print(f"You found the {obj} in your inventory.")
        if item_description:
            print(item_description)
        else:
            print(f"You look at the {obj} but find nothing of interest.")
    else:
        print("You can't look at that.")

def inventory_verb(inventory):
    """
    Handle the "inventory" verb action.
    """
    print("Inventory:")
    for item, quantity in inventory.view_inventory().items():
        print(f"- {item}: {quantity}")
