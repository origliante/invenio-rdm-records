import json

from flask_resources.serializers import JSONSerializer



class TestJSONSerializer(JSONSerializer):
    def dump_obj(self, obj):
        return obj

    def dump_list(self, obj_list):
        return obj_list

    #
    # Serialize to  JSON (obj and list)
    #
    def serialize_object(self, obj):
        """Dump the object into a JSON string."""
        o = self.dump_obj(obj)
        o = {'thisisatest': True}
        return json.dumps(o)

    def serialize_object_list(self, obj_list):
        """Dump the object list into a JSON string."""
        return json.dumps(self.dump_list(obj_list))

    def serialize_object_to_dict(self, obj):
        """Dump the object into a JSON string."""
        return self.dump_obj(obj)

    def serialize_object_list_to_dict(self, obj_list):
        """Dump the object list into a JSON string."""
        return self.dump_list(obj_list)
