from list_node import ListNode
from doublelinkedlist import DoubleLinkedList

list = DoubleLinkedList()
list.append(3)
list.append(5)
list.append(8)
list.append(23)
print("*"*40)
print("Lista Doblemente Enlazada")
print(list.__str__())
print("")
print("*"*40)
print("Cantidad de elementos de la lista:")
print(list.__len__())
print("*"*40)
print("Metodo get_item key(3):",list.__getitem__(3))
print("Devuelve el elemento ubicado en la posición indicada por key")
print("*"*40)
list.__setitem__(2, 67)
print("En la posición indicada por key se va a colocar un nuevo valor.")
print("Metodo set_item Key(2) Valor(67)")
print(list.__str__())
print("*"*40)
list.__delitem__(1)
print("Elimina de la estructura el elemento ubicado en la posición key.")
print("Metodo del_item Key(1)")
print(list.__str__())
print("*"*40)
print("Indica si la estructura está vacía.")
print("Metodo is_empty:",list.is_empty())
print("*"*40)
print("Visita desde el principio hacia el final todos los nodos de la lista y retorna sus elementos")
print("Metodo iter")
print(next(list.__iter__()))
print("*"*40)