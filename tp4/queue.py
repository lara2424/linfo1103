#! /usr/bin/python3

class Queue:
   
    def __init__(self):
        """
        pre: une queue
        post: initialise la queue
        """
        self.items = []


    def __len__(self):
        """
        pre: une queue
        post: la taille de la queue
        """
        return len(self.items)

    def enqueue(self, item):
        """
        pre: une queue et l element a ajouter
        post: une queue avec l element item en fin de queue
        """
        self.items.insert(0, item)
        return None

    def dequeue(self):
        """
        pre: un queue
        post: l'element qui a ete retirer de la queue
        """
        return self.items.pop()

    def is_empty(self):
        """
        pre: une queue
        post: true si vide
        """
        return self.items == []

    ########################################################
    # Si vous le désirez, vous pouvez implémenter la méthode
    # __str__(self) pour obtenir une représentation de votre
    # file sous forme de string
    # Exemple:
    def __str__(self):
        str_queue = "This is a Queue. Ideally, I should report " \
                    "my content.\n"

        return str_queue


# Exemples de tests:
file = Queue()
items = [i for i in range(1, 50)]

if not file.is_empty():
    print("Une nouvelle file devrait être vide après initialisation.")

for item in items:
    file.enqueue(item)
    if not len(file) == item:
        print("La taille de la file ({}) est incorrecte après ajout de l'élément : {}.".format(len(file), item))

for item in items:
    if not file.dequeue() == item:
        print("La suppression d'un élément ne renvoit pas le bon élément : {}.".format(item))

