#routes/dashboard.py
from flask import session
from flask_classful import FlaskView, route
from controllers.dashboard.signup import Signup

class Dashboard(FlaskView):
  def __init__(self):
    super().__init__()
    self.signup = Signup()

  @route('/')
  def dashboard_index(self):
    return "Dashboard"
    
  @route('/signup/', methods={'GET', 'POST'})
  def dashboard_signup(self):
    return self.signup.signup()