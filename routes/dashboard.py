#routes/dashboard.py
from flask_classful import FlaskView, route
from controllers.dashboard.signup import Signup
from controllers.dashboard.index import Index

class Dashboard(FlaskView):
  def __init__(self):
    super().__init__()
    self.signup = Signup()
    self.index = Index()

  @route('/')
  def dashboard_index(self):
    return self.index.index()

  @route('/logout/')
  def logout(self):
    return self.index.logout()
    
  @route('/signup/', methods={'GET', 'POST'})
  def dashboard_signup(self):
    return self.signup.signup()