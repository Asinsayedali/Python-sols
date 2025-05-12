class asinexecption(Exception):
    def __init__(self, message="Asin name is not allowed"):
        self.message = message
        super().__init__(self.message)


try:
    a = input("enter the name")
    if a == "Asin":
        raise asinexecption()
except Exception as e:
    print(e)
else:
    print("try got executed")
finally:
    print("Just executed")
