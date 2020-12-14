#controllers/login.py
import config, copy, lib
from flask import render_template, redirect, request, session
from datetime import datetime
from models.userdb import Userdb

class Login():
  def __init__(self):
    self.userdb = Userdb()

  def set_root(self):
    vlib = lib.Lib()
    vdatetime = vlib.get_timezone()
    date = datetime.strptime(vdatetime[0], "%d/%m/%Y")
    time = datetime.strptime(vdatetime[1], '%H:%M:%S')

    self.userdb.insert('root', 'etv@website.com', 'root', 'Admin', '', date, time, 'root')

  def check_user(self):
    vdict = copy.deepcopy(config.vdict)
    vdict['site_title'] = 'ទំព័រ​ចុះឈ្មោះ'

    if (request.method == 'POST'):
      email = request.form['femail']
      password = request.form['fpassword']

      if(self.userdb.check_user(email, password)):
        session['logged-in'] = email
        return redirect('/dashboard/')
        
    else:
      if 'logged-in' in session:
        return redirect('/dashboard/')

      user = self.userdb.select(1)
      if not user:
        self.set_root()

    return render_template('login.html', data=vdict)
