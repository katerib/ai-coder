class Objects:
    def __init__(self, data):
        self.objects = data

    def get_object(self, object_name):
        return self.objects[object_name]
