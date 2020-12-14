#templates/dashboard/index.py
import config, copy, lib
from flask import render_template, request, session, redirect
from models.userdb import Userdb

class Index():
  def __init__(self):
    self.userdb = Userdb()

  def index(self):
    vdict = copy.deepcopy(config.vdict)
    vdict['site_title'] = "ទំព័រ​គ្រប់គ្រង"

    if 'logged-in' in session:
      return render_template('dashboard/index.html', data=vdict)

    return redirect('/login/')

  def logout(self):
    session.pop('logged-in', None)
    return redirect('/')