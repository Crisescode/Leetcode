class Singleton(type):
    _instance = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instance:
            cls._instance[cls] = super(Singleton, cls).__class__(*args, **kwargs)

        return cls._instance[cls]


class Foo(metaclass=Singleton):
    pass


print(id(Foo()) == id(Foo()))


def singlon(cls):
    _instance = {}

    def warpper():
        if cls not in _instance:
            _instance[cls] = cls()

        return _instance[cls]

    return warpper


@singlon
class Foo2(object):
    pass


print(id(Foo2()) == id(Foo2()))
