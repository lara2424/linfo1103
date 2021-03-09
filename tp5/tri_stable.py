class book():
    """
    Classe représentant un livre, correspondant à une paire nom-année d'édition
    """

    def __init__(self, name, year):
        '''Constructuer de la classe Book'''
        self.name = name
        self.year = year

    def __lt__(self, other):
        '''Permet de comparer deux éléments. Correspond à l'opérateur <'''
        if isinstance(other, book):  # Test si l'autre élément est également un objet de type book
            return self.year < other.year  # Si c'est le cas, renvoie le résultat de la comparaison des dates d'edition
        else:
            return NotImplemented  # Sinon, indique que la comparaison n'est pas implémentée

    def __le__(self, other):
        '''Permet de comparer deux éléments. Correspond à l'opérateur <='''
        if isinstance(other, book):
            return self.year <= other.year
        else:
            return NotImplemented

    def __eq__(self, other):
        '''Permet de comparer deux éléments. Correspond à l'opérateur =='''
        if isinstance(other, book):
            return self.year == other.year
        else:
            return NotImplemented

    def __str__(self):
        return '{date}: {name}'.format(date=self.year, name=self.name)


def selection_sort_stable(books):
    """
    pre: `books` est un tableau (list) de `book`
    post: tri par sélection STABLE du tableau passé en paramètre.
        Les éléments sont triés en place
    """
    for i in range(len(books)-1):
        b_min = i
        for j in range(i + 1, len(books)):
            if books[j].year < books[b_min].year:
                b_min = j
        if b_min != i:
            tempo = books[b_min]
            for z in range(b_min-i):
                books[b_min]=books[b_min-1]
                b_min=b_min-1
            books[i]= tempo

    return books


############
# Exemple de test:

# Crée une liste de livres
library = [
    book(' Lincroyable Histoire 0', 2020),
    book('incroyable Histoire 0 (reéd. 1)', 2021),
    book('incroyable Histoire 0 (reéd. 2)', 2022),
    book('ncroyable Histoire 1', 2023),
    book('ncroyable Histoire 1 (reéd. 1)', 2021)
]

# Trie en place les libres de la bibliothèque
selection_sort_stable(library)
