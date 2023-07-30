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
        for obj_key in self.objects:
            obj = self.objects[obj_key]
            if obj['name'].lower() == object_name.lower():
                return obj
        return None

    
    def set_object_presence(self, item_name, is_present):
        item = self.get_object(item_name)

        if item:
            item["isPresent"] = is_present
