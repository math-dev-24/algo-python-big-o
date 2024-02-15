# L'affichage se fait via la console
# N'importez pas de module de liste chaînée déjà existant, le but est de créer votre propre code
# Gestion des messages d'erreurs
# Réfléchissez aux performances de votre algo qui devra être pensé pour pouvoir gérer un nombre conséquent de données.
# (Renseignez vous aussi sur les différences de performance entre une liste chaînée simple et double).


# Précisions sur les fonctions à développer :

# (OK) print(llist)-> str affiche la chaîne de caractères pour représenter le contenu de la liste
# (OK) append(value:int|str)-> None permet d'ajouter un élément à la fin de la liste
# (OK) insert(index:int, value:int|str)-> None insère un élément à l'index donné
# (OK) at_index(index)-> int|str renvoie la valeur à l'index donné
# (OK) preprend
# (OK) index_of(value:int|str)-> int renvoie l'index de la première valeur rencontrée, -1 si value n'est pas présente dans la liste
# (OK) is_unique()-> bool vérifie que la liste ne contient pas de doublons -> O(n!)
# (OK) contains(value:int|str)-> bool vérifie que value est présent dans la liste
# (OK) remove_at(index:int)-> None retire un élément à l'index donné
# (OK) reversed()-> None inverse le sens de la liste chaînée
# (OK) llist.lenght() / len(llist)-> int renvoie le nombre d'éléments contenus dans la liste chaînée, passée en argument

class Node:
    def __init__(self, data: str | int):
        self.data = data
        self.next, self.prev = None, None


class Llist:
    def __init__(self):
        self.head, self.tail = None, None
        self.length = 0

    def __str__(self):
        # Indice O(n)
        current = self.head
        elements = []
        while current:
            elements.append(repr(current.data))
            current = current.next
        return "[" + ", ".join(elements) + "]"

    def __len__(self) -> int:
        # Indice O(1)
        return self.length

    def append(self, data: str | int) -> None:
        # indice BigO = O(1)
        new_node: Node = Node(data)
        self.length += 1
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def prepend(self, data: str | int) -> None:
        # indice BigO = O(1)
        new_node: Node = Node(data)
        self.length += 1
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def insert(self, index: int, data: str | int) -> None:
        # j'utilise get_node_with_index et len qui est o(n) -> donc o(n)
        max_index: int = len(self)
        if index < 0:
            raise ValueError('Index ne peu pas être inférieur à 0')
        if index > max_index:
            raise ValueError("L'index est trop grand !")
        if index == 0:
            self.prepend(data)
        elif index == max_index:
            self.append(data)
        else:
            new_node: Node = Node(data)
            # je boucle jusqu'à trouver ma node -1
            # mon current est ma node et ma node.next doit etre la new node
            current: Node = self.get_node_with_index(index - 1)
            # __ le next node de la new node doit être la next node de la current node
            next_node = current.next
            current.next = new_node
            # ___
            new_node.prev = current
            new_node.next = next_node
            # ___
            next_node.prev = new_node
        self.length += 1

    def remove_at(self, index: int) -> None:
        # indice O(1) -> mais j'utilise get_node_with_index qui est O(n) -> donc O(n)
        max_index = len(self) - 1
        if index < 0:
            raise ValueError('Index ne peu pas être inférieur à 0')
        if index > max_index:
            raise ValueError("L'index est trop grand")
        if index == 0:
            self.head = self.head.next
            self.head.prev = None
        elif index == max_index:
            self.tail = self.tail.prev
            self.tail.next = None
        else:
            current: Node = self.get_node_with_index(index)
            prev_current: Node = current.prev
            next_current: Node = current.next
            prev_current.next = next_current
            next_current.prev = prev_current
        self.length -= 1

    def at_index(self, index: int) -> str:
        # indice : O(n) dépendant de get_node_with_index
        return self.get_node_with_index(index).data

    def index_of(self, data: str | int) -> int:
        # indice : O(n)
        if not self.head:
            return -1
        index = 0
        current = self.head
        while current:
            is_ok = current.data == data
            if is_ok:
                return index
            # increment de l'index
            current = current.next
            index += 1
        return -1

    def get_node_with_index(self, index: int) -> Node:
        # ___return Node with index
        # indice O(n)
        current = self.head
        for _ in range(index):
            current = current.next
        return current

    def is_unique(self) -> bool:
        # double boucle indice O(n^2) -> pas performant
        # utiliser une collection O(n)
        if not self.head:
            return True
        seen_data = set()
        current_node = self.head

        while current_node:
            if current_node.data in seen_data:
                return False
            seen_data.add(current_node.data)
            current_node = current_node.next
        return True

    def contains(self, data: str | int) -> bool:
        # Dépendant de index_of - > indice O(n)
        if self.index_of(data) != -1:
            return True
        else:
            return False

    def reversed(self):
        if not self.tail:
            return
        current = self.head
        prev = None
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev
        self.tail = current


if __name__ == '__main__':
    llist = Llist()
    print(llist) # -> []

    llist.append(3)
    llist.append(10)
    llist.append(30)
    print(len(llist)) # -> 3
    print(llist) # -> [3, 10, 30]

    llist.insert(1, 50)
    print(llist) # -> [3, 50, 10, 30]

    llist.remove_at(0)
    print(llist)#  -> [50, 10, 30]

    print(llist.contains(10)) # -> True
    print(llist.contains(87)) # -> False

    print(llist.index_of(10)) # -> 1
    print(llist.index_of(87)) # -> -1

    print(llist.at_index(1)) # -> 10

    print(llist.is_unique()) # -> True
    llist.append(50)
    print(llist) # -> [50, 10, 30, 50]
    print(llist.is_unique()) # -> False

    llist.append(20)
    llist.append(100)
    llist.append("test")
    print(llist) # -> [50, 10, 30, 50, 20, 100, "test"]
    llist.reversed()
    print(llist) # -> ["test", 100, 20, 50, 30, 10, 50]
