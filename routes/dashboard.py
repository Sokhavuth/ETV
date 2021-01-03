#routes/dashboard.py
import asyncio
from flask_classful import FlaskView, route
from controllers.dashboard.user import User
from controllers.dashboard.index import Index
from controllers.dashboard.movie import Movie
from controllers.dashboard.series import Series

class Dashboard(FlaskView):
  def __init__(self):
    super().__init__()
    
  @route('/')
  def dashboard_index(self):
    self.index = Index()
    return self.index.index()

  @route('/logout/')
  def dashboard_logout(self):
    self.index = Index()
    return self.index.logout()
    
  @route('/user/signup/', methods=['GET', 'POST'])
  def dashboard_signup(self):
    self.user = User()
    return self.user.signup()

  @route('/user/edit/<id>')
  def dashboard_edit(self, id):
    self.user = User()
    return self.user.edit(id)

  @route('/user/delete/<id>')
  def dashboard_delete(self, id):
    self.user = User()
    return self.user.delete(id)

  @route('/user/load/')
  def load_user(self):
    self.user = User()
    return self.user.load()

  @route('/movie/', methods=['GET', 'POST'])
  def dashboard_movie(self):
    self.movie = Movie()
    return self.movie.get_post()

  @route('/movie/delete/<id>')
  def dashboard_movie_delete(self, id):
    self.movie = Movie()
    return self.movie.delete(id)

  @route('/movie/edit/<id>')
  def dashboard_movie_edit(self, id):
    self.movie = Movie()
    return self.movie.edit(id)

  @route('/movie/load/')
  def dashboard_movie_load(self):
    self.movie = Movie()
    return self.movie.load()

  @route('/series/', methods=['GET', 'POST'])
  def dashborad_series(self):
    self.series = Series()
    return self.series.get_post()

  @route('/series/delete/<id>')
  def dashboard_series_delete(self, id):
    self.series = Series()
    return self.series.delete(id)

  @route('/series/edit/<id>')
  def dashboard_series_edit(self, id):
    self.series = Series()
    return self.series.edit(id)

  @route('/series/load/')
  def dashboard_series_load(self):
    self.series = Series()
    return self.series.load()