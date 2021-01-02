import random
class Météo:
    def __init__(self):
        self.météo={"soleil": 1, "vent" : 1}

    def Refresh_météo(self):
        self.météo["soleil"]= random.randint(0,1)
        self.météo["vent"]= random.randint(0,1)

    def get_Météo(self):
        return self.météo

    def __str__(self):
        return str(self.météo)
