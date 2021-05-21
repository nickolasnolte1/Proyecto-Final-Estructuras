from flask import Flask, request, redirect, url_for, render_template
from jinja2 import Template, Environment, FileSystemLoader
import json
from LinkedList import Node, LinkedList
import hashlib

app = Flask (__name__)

file = FileSystemLoader('templates')
environment = Environment(loader=file)

listaL = LinkedList()
lista = []

with open ('passwords.json') as json_file:
  my_json = json.load (json_file)

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



lista_artistas = list(artist_viernes.items())
lista_artistas2 = list(artist_sabado.items())

Lista_comp = lista_artistas + lista_artistas2


def linkedlist_artistas():
  lista = []
  for key, var in artist_viernes.items():
    string = key + var
    lista.append (string)
    print (string)
  listaL.head = (Node(lista[0]))
  for key, var in artist_sabado.items():
    string2 = key + var
    lista.append (string2)
    print (string2)
  lista.pop(0)
  for i in lista:
    listaL.insert_last(Node(i))

def sort_dic(token):
  sortedDict = dict(sorted(artist_viernes.items(), key=lambda x: x[0].lower()) )

  for k,v in sortedDict.items():
    return('{}:{}'.format(k,v))

def searches (token):
  #search = input("Ingrese el nombre del artista que desea buscar: ")
  if token in artist_viernes.keys() or token in artist_sabado.keys(): 
    return token

  else:
    return False


def hash (token):
  nombre_to_password = token
  str = hashlib.md5(nombre_to_password.encode('utf-8'))
  text_hashed = str.hexdigest()
  for i in my_json.keys():
    if text_hashed == my_json['names']:
      return text_hashed


#Se levanta el api con flask
@app.route ('/', methods = ['GET', 'POST'])
def homepage():
  find = request.args.get ("find","")
  html = environment.get_template('Index.html')
  Background = url_for ('static', filename = 'packground.png')
  logo = url_for ('static', filename = 'LOGO.png')
  if (find):
    return redirect(url_for('search', token = find))

  return html.render(Background = Background, logo = logo)

@app.route ('/LineUp', methods = ['GET', 'POST'])
def LineUp():
  sorting = request.args.get ("order", "")
  find = request.args.get ("find","")

  html = environment.get_template('LineUp.html')
  Background = url_for ('static', filename = 'packground.png')
  logo = url_for ('static', filename = 'LOGO.png')
  live = url_for ('static', filename = 'live.png')
  dua_lipa = url_for ('static', filename = 'dualipa.png')
  post = url_for ('static', filename = 'post.png')
  mcr = url_for ('static', filename = 'mcr1.png')
  jb = url_for ('static', filename = 'JB.png')
  kanye = url_for ('static', filename = 'kanye.png')
  dababy = url_for ('static', filename = 'dababy.png')
  god = url_for ('static', filename = "god.png")
  Mother = url_for ('static', filename = "Mother.png")
  if (find):
    return redirect (url_for('search', token = find))
  elif (sorting):
    return 
  return html.render (Background = Background, logo = logo, live = live, dua_lipa = dua_lipa, post = post, mcr = mcr, jb = jb, kanye = kanye, dababy = dababy, god = god, Mother = Mother, texto = Lista_comp)

@app.route ('/sort', methods = ['GET', 'POST'])
def sortedlist():
  return render_template('sort.html')
  

@app.route ("/search/<token>")
def search (token):
  name = searches(token)
  return render_template("search.html", name = name)
  
@app.route ('/VIP', methods = ['GET', 'POST'])
def hashing():
  find = request.args.get ("find" , "")
  hashing = request.args.get ("hash" , "")
  if(find):
    return redirect(url_for('search', token = find))

  return render_template('VIP.html', hashing = hashing)
  
@app.route ("/sort/ <token>")
def sorting (token):
  sort = sort_dic(token)
  return render_template('sort.html', sort = sort)


if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True)

