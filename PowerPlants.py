class PowerPlants:
    def __init__(self,météo, production = 0, cost = 1, co2 = 1):
        self.production = production
        self.cost = cost
        self.co2 = co2
        self.météo=météo
        
    def get_Production(self):
        return self.production
    def __str__(self):
        return "I am a PowerPlant"

class Centrale_Gaz(PowerPlants):
    def __init__(self, météo,maximum = 40, production = 10, cost = 1, co2=1):
        super().__init__(météo,production=production,cost=cost,co2=co2)
        self.maximum = maximum
    def change_production(self,new_production):
        if new_production> self.maximum:
            self.production=self.maximum
        elif new_production<=0:
            self.production = 0
        else:
            self.production = new_production

    def __str__(self):
        return 'centrale à Gaz : Je produis {}, pour un coût de {}, et je produis {} de Co2\n Je peux produire maximum {} d\'électricité'.format(self.production, self.production*self.cost,self.production*self.co2,self.maximum)



class Centrale_Nuc(PowerPlants):
    def __init__(self,météo, production = 10, cost = 1, co2=1):
        super().__init__(météo,production=production,cost=cost,co2=co2)

    def __str__(self):
        return 'Centrale Nucléaire : Je produis {}, pour un coût de {}, et je produis {} de Co2'.format(self.production, self.production*self.cost,self.production*self.co2)

class parc_éolien(PowerPlants):
    def __init__(self,météo,production = 10, cost=1,co2=0):
        super().__init__(météo,production=production,cost=cost,co2=co2)
    def get_Production(self):
        return self.production*self.météo.get_Météo()["vent"]
    def __str__(self):
        return 'Parc éolien : Je produis {}, pour un coût de {}, et je produis {} de Co2'.format(self.production, self.production*self.cost,self.production*self.co2)
class centrale_solaire(PowerPlants):
    def __init__(self,météo,production = 10, cost =1,co2 = 0):
        super().__init__(météo,production=production,cost=cost,co2=co2)
    def get_Production(self):
        return self.production*self.météo.get_Météo()["soleil"]
    def __str__(self):
        return 'Centrale Solaire : Je produis {}, pour un coût de {}, et je produis {} de Co2'.format(self.production, self.production*self.cost,self.production*self.co2)


