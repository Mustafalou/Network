class Noeud_Conc:
    def __init__(self):
        self.liste_powerplants=[]
    def Add(self,powerplant):
        self.liste_powerplants.append(powerplant)
    def Remove(self, powerplant):
        self.liste_powerplants.remove(powerplant)
    def return_liste(self):
        return self.liste_powerplants
    def get_All_Production(self):
        sum = 0
        for elem in self.liste_powerplants:
            sum+=elem.get_Production()
        return sum
