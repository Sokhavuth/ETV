#main.py
from flask import Flask
from routes.index import Index
 
app = Flask(__name__)
index = Index()
 
index.register(app, route_base='/')
 
if __name__ == '__main__':
  app.run(debug=True)