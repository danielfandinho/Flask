import datetime

from flask import Flask, render_template
app = Flask(__name__)  #Instaciamos / Name es un parametro

@app.route("/") #Esto es para que el localhost responda
def index():    #Funcion Index
    now=datetime.datetime.now() #Con esto conseguimos fecha y horas actuales
    new_year=now.month ==1 and now.day==1
    return render_template("index.html", new_year=new_year) #Retornamos
