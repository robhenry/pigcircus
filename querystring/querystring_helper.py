from urlparse import urlparse 
from cgi import parse_qs

if __name__ != '__lib__':
    def outputSchema(ignore):
        def wrapper(func):
            def inner(*args, **kwargs):
                return func(*args, **kwargs)
            return inner
        return wrapper

@outputSchema('chararray')
def parse_querystring_value(name, url):
    if url is None:
        return None

    query = urlparse(url).query
    values = parse_qs(query)

    if name not in values:
        return None

    return parse_qs(query)[name][0]
