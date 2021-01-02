Participant : 1,
matricule : 17292,
Nom et prénom: Yilmaz, Mustafa
# Simulation de réseau

## Diagramme de Classes
![Diag de classes](https://github.com/Mustafalou/Network/blob/main/Diagramme%20de%20classes.jpg)
## Diagramme de séquences
![Diag de séquences](https://github.com/Mustafalou/Network/blob/main/diaggrame%20de%20s%C3%A9quences.PNG)
## Documentation
Tout d'abord, installer kivy: étape à suivre dans ce lien :https://gist.github.com/qlurkin/343ac11da18bbda99f7150fd5fc80925
### Initialisation de Network.py:
dans Network.py, vous trouverez déja un example dinitialisation, pour pouvoir lancer le code:
![exemple d'init](https://github.com/Mustafalou/Network/blob/main/int.png)

En gros, il vous fait créer un dictionnaire network dans lequel vous allez ajouter tous les noeuds en pair(noeud_conc:noeud_distrib),
et ajouter les centrales électriques/clients dans les noeuds requis.

### les classes powerplants:
Elles ont toutes des attributs cout, production, et produciton de co2. Ainsi que des méthodes qui vont retourner leur production.
Seule la centrale à gaz a la capacité de changer sa production dans mon réseau.
La météo est dans chaque powerplant même si elle n'est nécessaire que dans les parcs solaires et les centrales solaires.

### les classes clients:
Elles ont toutes des attributs consommations et nom, même si le nom ne sert à rien ^^, et des méthodes qui vont retourner leur consommation

### les classes noeud_conc et noeud_distrib
Elles ont toutes les 2 des méthodes qui renvoient la valuer totale de consommation ou de production de leur liste respective.
Une méthode Add pour pouvoir rajouter un client à noeud_distrib et un powerplant à noeud_conc.
Ainsi que des méthodes pour supprimer que je n'ai pas utiliser dans les screenmanager.

### kivy:
J'ai utilisé le screenmanager de kivy pour avoir une meilleure vision du réseau, alors que si c'était que vace le terminal il n'y aurait peut-être pas eu de compréhension.
