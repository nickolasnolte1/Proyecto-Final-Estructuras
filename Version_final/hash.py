from LinkedList import Node, LinkedList
from main import artist_viernes
print ("")
artist_viernes = {
    "Dua Lipa": "9:30PM",
    "Post Malone": "10:30PM",
    "My chemical Romance": "11:30PM"
    }
artist_sabado = {
    "Justin Bieber": "7:30PM",
    "Kanye West": "8:30PM",
    "DaBaby": "9:30PM",
    "Childish Gambino": "10:30PM",
    "Mother Mother": "11:30PM"
}
listaL = LinkedList()
lista = []
lista2 = []

def linkedlist_artistas():
  for key, var in artist_viernes.items():
    string = key + var
    lista.append (string)
    #print (string)
  listaL.head = (Node(lista[0]))
  for key, var in artist_sabado.items():
    string2 = key + var
    lista.append (string2)
    lista2.append (string)
    lista2.append (string2)
    #print (string2)
  lista.pop(0)
  for i in lista:
    listaL.insert_last(Node(i))

def crear_listas():
  lista_artistas = list(artist_viernes.items())
  lista_artistas2 = list(artist_sabado.items())
  Lista_comp = lista_artistas + lista_artistas2
  print (Lista_comp)

crear_listas()

print (Lista_comp)
churro = linkedlist_artistas()

#print (lista2)
