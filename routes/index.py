#routes/index.py
import config, copy
from flask import render_template
from flask_classful import FlaskView, route
from controllers.login import Login
from controllers.home import Home
from controllers.movie import Movie
 
class Index(FlaskView):
  def __init__(self):
    super().__init__()
    self.login = Login()
    self.home = Home()
    self.movie = Movie()
 
  @route('/')
  def index(self):
    return self.home.get_youtube()

  @route('/login/', methods=['GET', 'POST'])
  def check_user(self):
    return self.login.check_user()

  @route('/user/<id>')
  def get_user(self, id):
    return "User"

  @route('/movie/<id>')
  def get_movie(self, id):
    return self.movie.get_movie(id)