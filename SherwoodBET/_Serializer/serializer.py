class Serializer:

    serialized = ['str', 'int', 'float', 'bool', 'NoneType']
    obj_extension = '_obj'

    @classmethod
    def serialize(self, obj):
        serialized = {}
        for field in obj.__class__._meta.local_fields:
            key = self.get_key(field)
            value = self.get_value(obj, field)
            serialized[key] = value
        return serialized

    @classmethod
    def get_key(self, field):
        return field.name if self.obj_extension not in field.name else field.name.split(self.obj_extension)[0]

    @classmethod
    def get_value(self, obj, field):
        value = getattr(obj, field.name)
        if type(value).__name__ in self.serialized:
            pass
        if type(value).__name__ == 'datetime':
            value = getattr(obj, field.name).isoformat()
        if self.obj_extension in field.name:
            value = str(getattr(obj, field.name))
        return value
