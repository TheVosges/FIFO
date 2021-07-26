class Line:
    pass

class Item_nextinline:
    pass

def make_line():
    """ Funkcja tworząca kolejkę

        Args:

        Returns:
            Line : zmienna będąca kolejką
    """
    line = Line()
    line.front = None
    line.back = None
    return line

def push(line, value):
    """ Funkcja dodająca wartość na koniec kolejki

        Args:
            line : do jakiej kolejki wartość ma zostać dodana
            value : zmienna która ma zostać dodana
        Returns:

    """
    if line.front is None: #Jeśli kolejka jest pusta zmienna dodana jest na przód kolejki
        item_nextinline = Item_nextinline() #tworzymy element "item_nextinlie"
        item_nextinline.value = value   #składający się z wartości orez referencji do poprzedniego i następnego elementu
        item_nextinline.after = None
        line.front = item_nextinline    
    elif line.back is None: #jeśli kolejka składa się z 1 elementu to nadpisujemy końcową zmienną
        item_nextinline = Item_nextinline() 
        item_nextinline.value = value   #wartość tego elementu
        item_nextinline.after = None
        line.back = item_nextinline     #nadpisujemy informacje ostatniego elementu kolejki
        item_nextinline = line.front    #nadpisujemy informacje pierwszego elementu kolejki
        item_nextinline.after = line.back #uzupełniając do jest za tym elementem
    else:   #jeśli w kolejce znajduje się ostatni i pierwszy element
        item_nextinline = Item_nextinline()
        item = line.back #zapisujemy dane poprzedniego elementu
        item_nextinline.value = value #ustawiamy wartość ostatniego elementu
        item_nextinline.after = None
        line.back = item_nextinline #nazywamy już że to jest ostatni element
        item.after = line.back #a informacje poprzedniego elementu uzupełniamy o referencje do ostatniego elementu


def pop(line):
    """ Funkcja wyjmująca pierwszy w kolejce element

        Args:
            line : kolejka z której element ma zostać wyjęty
        Returns:
            item_nextinline.value : wartość pierwszego w kolejce elementu
    """
    if line.front is None: #jeśli nie ma nic w kolejce to zwraca None
        return None
    item_nextinline = line.front #ładujemy informacje pierwszego w kolejce elementu
    line.front = item_nextinline.after #nadpusujemy pierwszy element referencją do poprzedniego
    return item_nextinline.value



