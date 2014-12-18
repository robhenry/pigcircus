import uuid 

if __name__ != '__lib__':
    def outputSchema(ignore):
        def wrapper(func):
            def inner(*args, **kwargs):
                return func(*args, **kwargs)
            return inner
        return wrapper

@outputSchema('uuid:chararray')
def create_uuid():
    return str(uuid.uuid1())
