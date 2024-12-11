class Father:
    def __init__(self):
        print("Fathers Constructor")
    def showPhone(self):
        print("Father's Phone")

class Mother:
    def showJewels(self):
        print("Mother's Jewels")

class Son(Father,Mother):
    def showPhone(self):
        print("Son's Phone")