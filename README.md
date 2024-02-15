# Exercice algo en python | BigO

- L'affichage se fait via la console
- N'importez pas de module de liste chaînée déjà existant, le but est de créer votre propre code
- Gestion des messages d'erreurs
- Réfléchissez aux performances de votre algo qui devra être pensé pour pouvoir gérer un nombre conséquent de données.
- (Renseignez vous aussi sur les différences de performance entre une liste chaînée simple et double).


### Précisions sur les fonctions à développer :

- (OK) print(llist)-> str affiche la chaîne de caractères pour représenter le contenu de la liste
- (OK) append(value:int|str)-> None permet d'ajouter un élément à la fin de la liste
- (OK) insert(index:int, value:int|str)-> None insère un élément à l'index donné
- (OK) at_index(index)-> int|str renvoie la valeur à l'index donné
- (OK) preprend
- (OK) index_of(value:int|str)-> int renvoie l'index de la première valeur rencontrée, -1 si value n'est pas présente dans la liste
- (OK) is_unique()-> bool vérifie que la liste ne contient pas de doublons -> O(n!)
- (OK) contains(value:int|str)-> bool vérifie que value est présent dans la liste
- (OK) remove_at(index:int)-> None retire un élément à l'index donné
- (OK) reversed()-> None inverse le sens de la liste chaînée
- (OK) llist.lenght() / len(llist)-> int renvoie le nombre d'éléments contenus dans la liste chaînée, passée en argument

### Test à faire :

- llist = Llist()
- print(llist) # -> []

- llist.append(3)
- llist.append(10)
- llist.append(30)
- print(len(llist)) # -> 3
- print(llist) # -> [3, 10, 30]

- llist.insert(1, 50)
- print(llist) # -> [3, 50, 10, 30]

- llist.remove_at(0)
- print(llist) # -> [50, 10, 30]

- print(llist.contains(10)) # -> True
- print(llist.contains(87)) # -> False

- print(llist.index_of(10)) # -> 1
- print(llist.index_of(87)) # -> -1

- print(llist.at_index(1)) # -> 10

- print(llist.is_unique()) # -> True
- llist.append(50)
- print(llist) # -> [50, 10, 30, 50]
- print(llist.is_unique()) # -> False

- llist.append(20)
- llist.append(100)
- llist.append("test")
- print(llist) # -> [50, 10, 30, 50, 20, 100, "test"]
- llist.reversed()
- print(llist) # -> ["test", 100, 20, 50, 30, 10, 50]
