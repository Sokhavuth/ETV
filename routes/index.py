#routes/index.py
import config, copy
from flask import render_template
from flask_classful import FlaskView, route
from controllers.login import Login
from controllers.movie import Movie
 
class Index(FlaskView):
  def __init__(self):
    super().__init__()
    self.login = Login()
    self.movie = Movie()
 
  @route('/')
  def index(self):
    vdict = copy.deepcopy(config.vdict)
    return render_template('index.html', data=vdict)

  @route('/login/', methods=['GET', 'POST'])
  def check_user(self):
    return self.login.check_user()

  @route('/user/<id>')
  def get_user(self, id):
    return "User"

  @route('/movie/<id>')
  def get_movie(self, id):
    return self.movie.get_movie(id)