#routes/index.py
from flask import render_template
from flask_classful import FlaskView, route
 
class Index(FlaskView):
  def __init__(self):
    super().__init__()
 
  @route('/')
  def index(self):
    return render_template('index.html', data={'siteTitle':'ទូរទស្សន៍​យើង'})