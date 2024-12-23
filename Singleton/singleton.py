class ClassicSingleton:
    # Class level variable to store the single class instance
    _instance = None

    # Override the __init__ method to control initialization
    def __init__(self):
        # Raise an error to prevent contructor utilization
        raise RuntimeError("Call instance() instead")

    @classmethod
    def get_instance(cls):
        if not cls._instance:  # Lazy instantiation
            # Create new instance of the class
            cls._instance = cls.__new__(cls)

        # Return the single instance of the class,
        # either newly created or existing
        return cls._instance


class Singleton:
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super().__new__(cls)

        return cls._instance


class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwds):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwds)
            cls._instances[cls] = instance

        return cls._instances[cls]


class SingletonDerived(metaclass=SingletonMeta):
    def some_logic(self):
        print("Some logic...")


class SingletonMeta2(type):
    _instances = {}

    def __init__(cls, name, bases, dct):
        super().__init__(name, bases, dict)
        cls._instances[cls] = super().__call__()

    def __call__(cls, *args, **kwds):
        return cls._instances[cls]


class SingletonDerived2(metaclass=SingletonMeta2):
    def __init__(self):
        pass


# s1 = ClassicSingleton()
# s1 = ClassicSingleton.get_instance()
# print(f"Classic Singleton: {s1}")

# s2 = Singleton()
# print(f"Singleton: {s2}")

# s3 = SingletonDerived()
# print(f"Singleton Derived: {s3}")
# s3.some_logic()

s4 = SingletonDerived2()
print(f"Singleton Derived 2: {s4}")
