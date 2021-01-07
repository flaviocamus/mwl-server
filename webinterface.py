# hello_world.py
"""
interface web
funciones:
configuracion dicom:
aetitle, puerto
aetitles conocidos, reglas por aetitle
visor de registro de operacion
reinicio de la operacion
mapeos de datos??

"""

from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    index = open("index.html",'r')
    return index.read()


if __name__ == "__main__":
    app.run()




