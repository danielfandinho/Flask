from flask import Flask, render_template
app = Flask(__name__)  #Instaciamos / Name es un parametro

@app.route("/") #Esto es para que el localhost responda
def index():    #Funcion Index
    return render_template("index.html") #Retornamos

"""@app.route("/<string:name>") #Interpretara el nombre que pasa en la URL
def hello(name):
    #name=name.capitalize()
    return f"Hello, {name}!"
"""
