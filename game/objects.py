import json

class Objects:
    def __init__(self):
        with open('data/objects.json', 'r') as file:
            data = json.load(file)
        self.objects = data['objects']

    def serialize(self):
        return {"objects": self.objects}

    def deserialize(self, data):
        self.objects = data["objects"]

    def get_description(self, object_name):
        """Returns the description of the specified object"""
        object_data = self.get_object(object_name)
        if object_data:
            return object_data['description']
        else:
            return 'Object not found.'
    
    def get_interaction(self, object_name):
        """Returns the interaction of the specified object"""
        object_data = self.get_object(object_name)
        if object_data:
            return str(object_data['interaction'])
        else:
            return 'Object not found.'

    def get_object(self, object_name):
        """Returns the object data based on the given object name"""
        for obj_key, obj_value in self.objects.items():
            if obj_key.lower() == object_name.lower():
                return obj_value
        return None

    def mark_item_as_equipped(self, item_name):
        """Marks the specified item as equipped"""
        item_data = self.get_object(item_name)
        if item_data:
            item_data["equipped"] = True

    def handle_item_effect(self, item_name):
        """Handles the effect of using the specified item"""
        item_data = self.get_object(item_name)
        if item_data:
            print(item_data["effect"])
