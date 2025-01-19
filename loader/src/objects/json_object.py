import json

from src.objects.object import Object

class JsonObject(Object):
    def __init__(self, content : json):
        self.content = content
        self.mimtype = "json"

    def get_formated(self):
        return json.dumps(self.content)
