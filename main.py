from flask import Flask, request, redirect, url_for, render_template
from jinja2 import Template, Environment, FileSystemLoader
import LinkedList

app = Flask (__name__)

file = FileSystemLoader('templates')
environment = Environment(loader=file)

artist_viernes = {
    "Dua Lipa": "9:00PM",
    "Post Malone": "10:30PM",
    "My chemical Romance": "11:20PM"
    }

artist_sabado = {
    "Justin Bieber": "7:30PM",
    "Kanye West": "8:30PM",
    "DaBaby": "9:30PM",
    "Childish Gambino": "10:30PM",
    "Blackbear": "11:30PM"
}

def sort():
  sortedDict = dict(sorted(artist_viernes.items(), key=lambda x: x[0].lower()) )

  for k,v in sortedDict.items():
    print('{}:{}'.format(k,v))

def search ():
  search = input("Ingrese el nombre del artista que desea buscar: ")
  values = []
  if search in artist_viernes.keys() or search in artist_sabado.keys(): 
    for i in artist_viernes.items() and artist_sabado.items():
      if search in i:
        values.append(i)
    print (values)

  else:
    print ("No se encuentra el nombre en la lista, porfavor intentelo de nuevo...")

def hash ():
  pass
def main():
  pass

#Se levanta el api con flask
@app.route ('/homepage', methods = ['GET', 'POST'])
def homepage():
  html = environment.get_template('Index.html')
  Background = url_for ('static', filename = 'packground.png')
  logo = url_for ('static', filename = 'LOGO.png')
  return html.render(Background = Background, logo = logo)
#@app.route ('/lineup', methods = ['GET', 'POST'])


if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True)
