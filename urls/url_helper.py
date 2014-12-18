from urlparse import urlparse 

if __name__ != '__lib__':
    def outputSchema(ignore):
        def wrapper(func):
            def inner(*args, **kwargs):
                return func(*args, **kwargs)
            return inner
        return wrapper

@outputSchema('chararray')
def parse_url_part(part, url):
    if url is None:
        return None

    value = None

    if part == 'query':
        value = urlparse(url).query

    if part == 'scheme':
        value = urlparse(url).scheme

    if part == 'path':
       value = urlparse(url).path

    if part == 'netloc':
       value = urlparse(url).netloc

    if value == '':
        return None

    return value
