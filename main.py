#main.py
import config
from flask import Flask
from routes.index import Index
from routes.dashboard import Dashboard
 
app = Flask(__name__)
index = Index()
dashboard = Dashboard()

app.secret_key = config.vdict['secret_key']
 
index.register(app, route_base='/')
dashboard.register(app, route_base='/dashboard')
 
if __name__ == '__main__':
  app.run(debug=True)