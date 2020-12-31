#controllers/dashboard/user.py
import config, copy, lib, datetime
from flask import render_template, session, request, redirect
from models.userdb import Userdb

class User():
  def __init__(self):
    self.userdb = Userdb()
    self.lib = lib.Lib()

  def signup(self):
    vdict = copy.deepcopy(config.vdict)
    vdict['site_title'] = "ទំព័រ​អ្នក​ប្រើប្រាស់"
    vdict['datetime'] = self.lib.get_timezone()
    session['page'] = 0

    if request.method == "POST":
      username = request.form['fusername']
      content = request.form['fcontent']
      password = request.form['fpassword']
      role = request.form['frole']
      date = request.form['fdate']
      time = request.form['ftime']
      email = request.form['femail']
      edit_id = request.form['fedit-id']

      if not email:
        vdict['message'] = 'ចាំបាច់​ត្រូវ​មាន​ E-MAIL!'
        return render_template('dashboard/user.html', data=vdict)

      if (self.userdb.check_email(email)) and (not edit_id):
        vdict['message'] = 'E-MAIL នេះ​ត្រូវ​បាន​គេ​យក​ទៅ​ប្រើប្រាស់​ហើយ។'
        return render_template('dashboard/user.html', data=vdict)

      if 'logged-in' in session:
        author_id = session['author-id']
        author_role = self.userdb.check_author(author_id)
        author = author_role[1]
      else:
        author = 'root'

      try:
        date = datetime.datetime.strptime(date, "%d/%m/%Y")
      except ValueError:
        vdict['message'] = 'ទំរង់​កាលបរិច្ឆេទ​មិន​ត្រឹមត្រូវ!'
        return render_template('dashboard/user.html', data=vdict)

      try:
        time = datetime.datetime.strptime(time, "%H:%M:%S")
      except ValueError:
        vdict['message'] = 'ទំរង់​ពេល​វេលា​មិន​ត្រឹមត្រូវ!'
        return render_template('dashboard/user.html', data=vdict)

      if edit_id:
        if author_role[4] == 'Admin':
          self.userdb.update(username, email, password, role, content, date, time, author, edit_id)
      else:
        if author_role[4] == 'Admin':
          self.userdb.insert(username, email, password, role, content, date, time, author)

      vdict['users'] = self.userdb.select(vdict['dashboard_max_post'])
      vdict['thumbs'] = self.lib.get_thumbs(vdict['users'], 5, type='user')
      return render_template('dashboard/user.html', data=vdict)

    elif 'logged-in' in session:
      vdict['users'] = self.userdb.select(vdict['dashboard_max_post'])
      vdict['thumbs'] = self.lib.get_thumbs(vdict['users'], 5, type='user')
      return render_template('dashboard/user.html', data=vdict)
    else:
      return redirect('/login/')

  def edit(self, id):
    vdict = copy.deepcopy(config.vdict)
    vdict['blog_title'] = 'កែតំរូវ​អ្នក​ប្រើប្រាស់'
    vdict['edit-id'] = id

    if 'logged-in' in session:
      vdict['users'] = self.userdb.select(vdict['dashboard_max_post'])
      vdict['thumbs'] = self.lib.get_thumbs(vdict['users'], 5, type='user')
      vdict['user'] = self.userdb.select(id=id)
      date = (vdict['user'][6]).strftime('%d/%m/%Y')
      time = (vdict['user'][7]).strftime('%H:%M:%S')
      vdict['datetime'] = (date, time)

      return render_template('dashboard/user.html', data=vdict)

    return redirect('/login/')

  def delete(self, id):
    author_id = session['author-id']
    author_role = self.userdb.check_author(author_id)
    if author_role[4] == 'Admin':
      self.userdb.delete(id)

    return redirect('/dashboard/user/signup/')

  def load(self):
    if 'logged-in' in session:
      vdict = copy.deepcopy(config.vdict)
      session['page'] += 1
      vdict['users'] = self.userdb.select(vdict['dashboard_max_post'], page=session['page'])
      vdict['thumbs'] = self.lib.get_thumbs(vdict['users'], 5, type="user")

      new_list = []
      for user in vdict['users']:
        new_user = list(user)
        new_user[6] = user[6].strftime('%d/%m/%Y') 
        new_user[7] = user[7].strftime('%H:%M:%S') 
        new_list.append(new_user)

      vdict['users'] = new_list
      return vdict
    else:
      return render_template('login.html', data=vdict)