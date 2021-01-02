class Noeud_Distrib:
    def __init__(self):
        self.liste_customers=[]
    def Add(self,powerplant):
        self.liste_customers.append(powerplant)
    def Remove(self, powerplant):
        self.liste_customers.remove(powerplant)
    def return_liste(self):
        return self.liste_customers
    def get_All_Consommation(self):
        somme = 0
        for elem in self.liste_customers:
            somme+=elem.get_Consommation()
        return somme
