#routes/dashboard.py
from flask_classful import FlaskView, route
from controllers.dashboard.user import User
from controllers.dashboard.index import Index
from controllers.dashboard.movie import Movie
from controllers.dashboard.series import Series

class Dashboard(FlaskView):
  def __init__(self):
    #super().__init__()
    self.user = User()
    self.index = Index()
    self.movie = Movie()
    self.series = Series()

  @route('/')
  def dashboard_index(self):
    return self.index.index()

  @route('/logout/')
  def dashboard_logout(self):
    return self.index.logout()
    
  @route('/user/signup/', methods=['GET', 'POST'])
  def dashboard_signup(self):
    return self.user.signup()

  @route('/user/edit/<id>')
  def dashboard_edit(self, id):
    return self.user.edit(id)

  @route('/user/delete/<id>')
  def dashboard_delete(self, id):
    return self.user.delete(id)

  @route('/user/load/')
  def load_user(self):
    return self.user.load()

  @route('/movie/', methods=['GET', 'POST'])
  def dashboard_movie(self):
    return self.movie.get_post()

  @route('/movie/delete/<id>')
  def dashboard_movie_delete(self, id):
    return self.movie.delete(id)

  @route('/movie/edit/<id>')
  def dashboard_movie_edit(self, id):
    return self.movie.edit(id)

  @route('/movie/load/')
  def dashboard_movie_load(self):
    return self.movie.load()

  @route('/series/', methods=['GET', 'POST'])
  def dashborad_series(self):
    return self.series.get_post()

  @route('/series/delete/<id>')
  def dashboard_series_delete(self, id):
    return self.series.delete(id)

  @route('/series/edit/<id>')
  def dashboard_series_edit(self, id):
    return self.series.edit(id)

  @route('/series/load/')
  def dashboard_series_load(self):
    return self.series.load()