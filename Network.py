from Météo import *
from PowerPlants import *
from Customers import *
from Noeud_Conc import *
from Noeud_Distrib import *
from kivy.app import App
#kivy.require("1.8.0")
import random
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen,FadeTransition
import time
#The big Networks that will contain all the lill networks
Network = {}
#The météo that we will change in every MAJ
Météo = Météo()
#Powerplants for Noeud_Concatenation 1
Centrale_gaz1 = Centrale_Gaz(Météo)
Centrale_nuc1= Centrale_Nuc(Météo)
centrale_solaire1 = centrale_solaire(Météo)
Noeud_Conc1 = Noeud_Conc()
for elem in [Centrale_gaz1, Centrale_nuc1,centrale_solaire1]:
    Noeud_Conc1.Add(elem)
#The first Noeud_Conc has been done
#Customers for Noeud_Distrib1
City1 = Ville()
Entreprise1 = Entreprise()
Dissipateur1 = Dissipateur()
Noeud_Distrib1 =Noeud_Distrib()
for elem in [Entreprise1,Dissipateur1,City1]:
    Noeud_Distrib1.Add(elem)
#We put évery Noeud like this in the Network
Network[Noeud_Conc1]= Noeud_Distrib1

Centrale_gaz2 = Centrale_Gaz(Météo)
Centrale_nuc2= Centrale_Nuc(Météo)
centrale_solaire2 = centrale_solaire(Météo)
Noeud_Conc2 = Noeud_Conc()
for elem in [Centrale_gaz2, Centrale_nuc2,centrale_solaire2]:
    Noeud_Conc2.Add(elem)
#The second Noeud_Conc has been done
#Customers for Noeud_Distrib2
City2 = Ville()
Entreprise2 = Entreprise()
Dissipateur2 = Dissipateur()
Noeud_Distrib2 =Noeud_Distrib()
for elem in [Entreprise2,Dissipateur2,City2]:
    Noeud_Distrib2.Add(elem)
#We put évery Noeud like this in the Network

Network[Noeud_Conc2]= Noeud_Distrib2


Buttons_to_Noeuds = {}
btn=0
class MainScreen(Screen):
    def show(self):
        pass
    

class One_Noeud(Screen):
    def show(self):
        global btn
        global Buttons_to_noeuds
        self.textinputs = []
        y=0.8
        self.noeud = Buttons_to_Noeuds[btn].return_liste()
        if btn.id =="C":
            self.add_widget(Label(text="Noeud de Distribution", size_hint = (1,0.1), pos_hint={"y":0.9} ))
            for elem in Buttons_to_Noeuds[btn].return_liste():
                self.add_widget(Label(text=elem.__str__(),size_hint= (0.7,0.1),pos_hint={"y":y}))

                y-=0.1
        else:
            self.add_widget(Label(text="Noeud de Concaténation", size_hint = (1,0.1), pos_hint={"y":0.9} ))
            igaz=0
            for elem in self.noeud:
                self.add_widget(Label(text=elem.__str__(),size_hint= (0.7,0.1),pos_hint={"y":y}))
                if type(elem) == type(Centrale_Gaz(1)):
                    self.textinputs.append(TextInput(hint_text = "new prod",size_hint = (0.2,0.1),pos_hint={"x":0.7,"y":y},multiline=False))
                    self.add_widget(self.textinputs[len(self.textinputs)-1])
                    self.add_widget(Button(text="ok",id = str(igaz),on_press = self.change_prod,size_hint = (0.1,0.1),pos_hint={"x":0.9,"y":y}))
                    igaz+=1
                y-=0.1
        self.add_widget(Button(text="Back",on_press=self.goback, size_hint=(1,0.2),pos_hint={"bottom":0}))
    def change_prod(self,btn):
        i=0
        for elem in self.noeud:
            if type(elem) == type(Centrale_Gaz(1)):
                if int(btn.id)==i:
                    elem.change_production(int(self.textinputs[i].text))
                    print("done")
                i+=1
        global Buttons_to_Noeuds
        Buttons_to_Noeuds = {}
        self.manager.current="noeuds"
        
    def goback(self,bouton):
        self.manager.current = "noeuds"
    def clr(self):
        self.clear_widgets()
class EachNoeudScreen(Screen):
    def show_Noeuds(self):
        global Météo
        self.météo = Météo
        global Network
        global Buttons_to_Noeuds
        
        self.add_widget(Label(text = "Noeuds Concaténations",size_hint=(0.5,0.1),pos_hint={"y":0.9}))
        self.add_widget(Label(text = "Noeuds Distributions",size_hint=(0.5,0.1),pos_hint={"x":0.5,"y":0.9}))
        y=0.79
        i=1
        Danger = 0
        for elem, value in Network.items():
            self.add_widget(Label(text=str(i), size_hint=(0.1,0.1),pos_hint={"y":y}))
            Buttons_to_Noeuds[Button(on_press=self.switch_screen,text = str(elem.get_All_Production()), size_hint = (0.45,0.1),pos_hint = {"x":0.1,"y":y},id="P")]=elem
            Buttons_to_Noeuds[Button(on_press=self.switch_screen,text = str(value.get_All_Consommation()), size_hint = (0.45,0.1),pos_hint = {"x":0.55,"y":y},id="C")]=value
            if elem.get_All_Production() > value.get_All_Consommation():
                Danger+=1
                y-=0.1
                self.add_widget(Label(text="SurProduction, diminuer la production de certains PowerPlants",size_hint=(1,0.1),pos_hint={"y":y}))
            elif elem.get_All_Production() < value.get_All_Consommation():
                Danger+=1
                y-=0.1
                self.add_widget(Label(text="SurConsommation, augmenter la production de certains PowerPlants",size_hint=(1,0.1),pos_hint={"y":y}))
            y-=0.1
            i+=1
        self.add_widget(Label(text = "La météo : {}".format(Météo.get_Météo()),size_hint=(0.5,0.1),pos_hint={"y":y}))
        for elem in Buttons_to_Noeuds.keys():
            self.add_widget(elem)
        self.add_widget(Label(text="Vous avez {} endroits à changer si vous voulez vous en sortir".format(Danger),size_hint=(0.5,0.1),pos_hint={"x":0.1,"y":0}))
        self.add_widget(Button(text="Main Menu",on_press = self.gotomain, size_hint=(0.2,0.1),pos_hint={"x":0.8,"y":0}))
        self.add_widget(Button(text="maj", on_press = self.refresh,size_hint=(0.5,0.1),pos_hint={"x":0.5,"y":y}))
    def refresh(self,btn):
        global Buttons_to_Noeuds
        self.météo.Refresh_météo()
        Buttons_to_Noeuds = {}
        self.manager.current="main"
        
    def gotomain(self,btn):
        self.manager.current = "main"
    def clr(self):
        self.clear_widgets()

    def switch_screen(self,bouton):
        self.manager.current = "1noeud"
        global btn
        btn = bouton
        
        
        
        


class ScreenManagement(ScreenManager):
    pass


    
presentation = Builder.load_file("main.kv")
class MainApp(App):
    def build(self):
        return presentation


if __name__== "__main__":
    MainApp().run()
