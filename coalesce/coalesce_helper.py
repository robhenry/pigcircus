if __name__ != '__lib__':
    def outputSchema(ignore):
        def wrapper(func):
            def inner(*args, **kwargs):
                return func(*args, **kwargs)
            return inner
        return wrapper

@outputSchema('val:chararray')
def coalesce(*arg):
    for el in arg:
        if el is not None:
            return el
    return None
