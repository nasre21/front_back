from flask import Flask, request
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app)
con = sqlite3.connect("weather.db")

cur = con.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS cities(id INTEGER PRIMARY KEY AUTOINCREMENT,id_city TEXT, nombre TEXT,temperatura INTEGER,rain_probability REAL)")

con.commit()
con.close()

@app.route("/")
def index():
     con = sqlite3.connect("weather.db")
     cur = con.cursor()
     response = cur.execute("SELECT * FROM cities")
     data = [{"id":row[0],"id_city":row[1],"nombre":row[2],"temperatura":row[3],"rain_probability":row[4]}for row in response]
     return data

@app.route("/weather", methods= ["POST"])
def weather():


     id = request.form["id"]
     id_city = request.form["id_city"]
     nombre = request.form["nombre"]
     temperatura = request.form["temperatura"]
     rain_probability = request.form["rain_probability"]

     con = sqlite3.connect("weather.db")
     cur = con.cursor()

     cur.execute("INSERT INTO weather (id, id_city,nombre, temperatura,rain_probability)VALUES(?,?,?,?,?)",(id,id_city, nombre,temperatura,rain_probability))

     con.commit()
     con.close()
     cur.close()

     return ""


     
if __name__ == "__main__":
     app.run(debug=True)