class Singletone:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            print("Creating new instance")
            cls._instance = super(Singletone, cls).__new__(cls)
        return cls._instance

ob1 = Singletone()
ob2 = Singletone()

print(ob1 is ob2)

