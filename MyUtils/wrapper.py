def iter2list(func):
    def wrapper(*args, **kwargs):
        return list(func(*args, **kwargs))
    return wrapper
