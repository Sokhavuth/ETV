#routes/dashboard.py
from flask_classful import FlaskView, route
from controllers.dashboard.user import User
from controllers.dashboard.index import Index
from controllers.dashboard.movie import Movie

class Dashboard(FlaskView):
  def __init__(self):
    super().__init__()
    self.user = User()
    self.index = Index()
    self.movie = Movie()

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