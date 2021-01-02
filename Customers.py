class Customer:
    def __init__(self, consommation = 1,name = "customer"):
        self.consommation=consommation
        self.name = name
    def get_Consommation(self):
        return self.consommation
    def __str__(self):
        return str(self.consommation)+" : "+self.name 

class Ville(Customer):
    def __init__(self,consommation=1,):
        super().__init__(consommation,name="ville")
class Entreprise(Customer):
    def __init__(self,consommation=1):
        super().__init__(consommation,name = "entreprise")

class Vente(Customer):
    def __init__(self,consommation=1):
        super().__init__(consommation,name="vente")

class Dissipateur(Customer):
    def __init__(self,consommation=10):
        super().__init__(consommation,name="dissipateur")



