from flask import Flask
app = Flask(__name__)  #Instaciamos / Name es un parametro

@app.route("/") #Esto es para que el localhost responda
def index():    #Funcion Index
    return "Hello, word" #Retornamos

"""
@app.route("/marcos") #Esto es una nueva ruta
def marcos():    #Funcion nombre
    return "Hello, Marcos" #Retornamos

@app.route("/juan") #Esto es una nueva ruta
def juan():    #Funcion nombre1
    return "Hello, Juan" #Retornamos
"""
