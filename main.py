#main.py
import config
from flask import Flask
from routes.index import Index
from routes.dashboard import Dashboard
 
app = Flask(__name__)

app.secret_key = config.vdict['secret_key']
 
Index.register(app, route_base='/')
Dashboard.register(app, route_base='/dashboard')
 
if __name__ == '__main__':
  app.run(debug=True)