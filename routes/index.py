#routes/index.py
import asyncio
from flask import render_template
from flask_classful import FlaskView, route
from controllers.login import Login
from controllers.home import Home
from controllers.movie import Movie
from controllers.country import Country
from controllers.series import Series
from controllers.country_series import Country_series
 
class Index(FlaskView):
  def __init__(self):
    super().__init__()
 
  @route('/')
  def index(self):
    self.home = Home()
    return self.home.get_youtube()
    
  @route('/login/', methods=['GET', 'POST'])
  def check_user(self):
    self.login = Login()
    return self.login.check_user()

  @route('/user/<id>')
  def get_user(self, id):
    return "User"

  @route('/movie/<id>')
  def get_movie(self, id):
    self.movie = Movie()
    return self.movie.get_movie(id)

  @route('/movie/country/<label>')
  def get_category(self, label):
    self.country = Country()
    return self.country.get_movie(label)

  @route('/movie/country/load/')
  def load_movie(self):
    self.country = Country()
    return self.country.load_movie()

  @route('/series/<id>')
  def get_series(self, id):
    self.series = Series()
    return self.series.get_series(id)

  @route('/series/country/<label>')
  def get_category_series(self, label):
    self.country_series = Country_series()
    return self.country_series.get_series(label)

  @route('/series/country/load/')
  def load_series(self):
    self.country_series = Country_series()
    return self.country_series.load_series()