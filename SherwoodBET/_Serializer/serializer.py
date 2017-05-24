class Serializer:

    serialized = [str, int, float, bool, type(None)]
    obj_extension = '_obj'

    @classmethod
    def serialize(cls, obj):
        if type(obj) is list:
            return [cls.serialize(elem) for elem in obj]
        if type(obj) is dict:
            serialized = {}
            for key in obj:
                serialized[key] = cls.serialize(obj[key])
            return serialized
        if type(obj) in cls.serialized:
            return obj
        if type(obj).__name__ == 'datetime':
            return obj.isoformat()
        serialized = {}
        for field in obj.__class__._meta.local_fields:
            key = cls.get_key(field)
            value = cls.get_value(obj, field)
            serialized[key] = value
        return serialized

    @classmethod
    def get_key(self, field):
        return field.name if self.obj_extension not in field.name else field.name.split(self.obj_extension)[0]

    @classmethod
    def get_value(self, obj, field):
        value = getattr(obj, field.name)
        if type(value) in self.serialized:
            pass
        if type(value).__name__ == 'datetime':
            value = getattr(obj, field.name).isoformat()
        if self.obj_extension in field.name:
            value = str(getattr(obj, field.name))
        return value
