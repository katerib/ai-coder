class Objects:
    def __init__(self, data):
        self.objects = data

    # This can probably be a method you modify for the description or just scrap and create your own
    def examine_object(self, object_name):
        """Prints the description of the specified object"""
        object_data = self.get_object(object_name)
        if object_data:
            print("Name:", object_data["name"])
            print("Description:", object_data["description"])
        else:
            print("Object not found.")
    
    # Possibly remove redundant methods replacement was use_item in text_Adventure class
    def use_object(self, object_name):
        """Performs an action when the specified object is used"""
        object_data = self.get_object(object_name)
        if object_data:
            print("Using", object_data["name"])
            # Implement the desired action for using the object
        else:
            print("Object not found.")

    # Possibly remove redundant methods replacement take_item in text_Adventure class
    def take_object(self, object_name):
        """Adds the specified object to the player's inventory"""
        object_data = self.get_object(object_name)
        if object_data:
            if object_data["equipped"]:
                print("You have already taken the", object_data["name"])
            else:
                object_data["equipped"] = True
                print("You took the", object_data["name"])
        else:
            print("Object not found.")

    # Cool to have but not sure if we need
    def is_object_obtained(self, object_name):
        """Checks if the specified object has been obtained"""
        object_data = self.get_object(object_name)
        if object_data:
            return object_data["equipped"]
        else:
            return False

    # Cool to have but not sure if we need
    def get_equipped_objects(self):
        """Returns a list of equipped objects"""
        equipped_objects = []
        for object_name, object_data in self.objects.items():
            if object_data["equipped"]:
                equipped_objects.append(object_name)
        return equipped_objects

    # ------------------Keep these methods for now------------------

    # Current methods that are being used within the game

    def get_object(self, object_name):
        """Returns the object data based on the given object name"""
        return self.objects.get(object_name)
    
    def mark_item_as_equipped(self, object_name):
        """Mark an item as equipped in the objects JSON."""
        object_data = self.get_object(object_name)
        if object_data:
            object_data["equipped"] = True

    def mark_item_as_not_equipped(self, item_name):
        """
        Mark an item as not equipped in the objects_data.
        """
        if item_name in self.objects:
            self.objects[item_name]["equipped"] = False

    def handle_item_effect(self, item_data):
        """
        Handle the effect of using an item.
        Implement the specific logic here based on the item's effect.
        """
        item_effect = item_data["effect"]
        print(item_effect)
