'''Importamos flask a nuestra instancia de python'''
from flask import Flask

app = Flask(__name__)
'''El test para ver si funciona'''
@app.route('/')
def hello():
    return "Hello Habib, its for you "

if __name__ == '__main__':
    app.run()