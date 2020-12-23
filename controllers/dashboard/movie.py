#controllers/dashboard/movie.py
import config, copy, lib, datetime, uuid
from flask import render_template, session, request, redirect
from models.userdb import Userdb
from models.moviedb import Moviedb

class Movie():
  def __init__(self):
    self.userdb = Userdb()
    self.lib = lib.Lib()
    self.moviedb = Moviedb()

  def get_post(self):
    vdict = copy.deepcopy(config.vdict)
    vdict['site_title'] = "ទំព័រ​ភាពយន្តទោល"
    vdict['datetime'] = self.lib.get_timezone()
    session['page'] = 0

    if (request.method == "POST") and ('logged-in' in session):
      vid = request.form['fvid']
      type = request.form['ftype']
      title = request.form['ftitle']
      content = request.form['fcontent']
      country = request.form['fcountry']
      date = request.form['fdate']
      time = request.form['ftime']
      author = session['logged-in']

      try:
        date = datetime.datetime.strptime(date, "%d/%m/%Y")
      except ValueError:
        vdict['message'] = 'ទំរង់​កាលបរិច្ឆេទ​មិន​ត្រឹមត្រូវ!'
        return render_template('dashboard/movie.html', data=vdict)

      try:
        time = datetime.datetime.strptime(time, "%H:%M:%S")
      except ValueError:
        vdict['message'] = 'ទំរង់​ពេល​វេលា​មិន​ត្រឹមត្រូវ!'
        return render_template('dashboard/movie.html', data=vdict)

      if 'edit-id' in session:
        id = session['edit-id']
        self.moviedb.update(vid, type, title, country, content, date, time, author, id)
        session.pop('edit-id', None)
      else:
        id = str(uuid.uuid4().int)
        self.moviedb.insert(id, vid, type, title, country, content, date, time, author)

      vdict['movies'] = self.moviedb.select(vdict['dashboard_max_post'])
      vdict['thumbs'] = self.lib.get_thumbs(vdict['movies'], 5, type='movie')
      return render_template('dashboard/movie.html', data=vdict)

    elif 'logged-in' in session:
      vdict['movies'] = self.moviedb.select(vdict['dashboard_max_post'])
      vdict['thumbs'] = self.lib.get_thumbs(vdict['movies'], 5, type='movie')
      return render_template('dashboard/movie.html', data=vdict)
    else:
      return redirect('/login/')

  def edit(self, id):
    vdict = copy.deepcopy(config.vdict)
    vdict['site_title'] = 'កែតំរូវ​ភាពយន្ត​ទោល'
    session['edit-id'] = id

    if 'logged-in' in session:
      vdict['movies'] = self.moviedb.select(vdict['dashboard_max_post'])
      vdict['thumbs'] = self.lib.get_thumbs(vdict['movies'], 5, type='movie')
      vdict['movie'] = self.moviedb.select(id=id)
      date = (vdict['movie'][6]).strftime('%d/%m/%Y')
      time = (vdict['movie'][7]).strftime('%H:%M:%S')
      vdict['datetime'] = (date, time)

      return render_template('dashboard/movie.html', data=vdict)

    return redirect('/login/')

  def delete(self, id):
    self.moviedb.delete(id)
    return redirect('/dashboard/movie/')

  def load(self):
    if 'logged-in' in session:
      vdict = copy.deepcopy(config.vdict)
      session['page'] += 1
      vdict['movies'] = self.moviedb.select(vdict['dashboard_max_post'], page=session['page'])
      vdict['thumbs'] = self.lib.get_thumbs(vdict['movies'], 5, type="movie")

      new_list = []
      for movie in vdict['movies']:
        new_movie = list(movie)
        new_movie[6] = movie[6].strftime('%d/%m/%Y') 
        new_movie[7] = movie[7].strftime('%H:%M:%S') 
        new_list.append(new_movie)

      vdict['movies'] = new_list
      return vdict
    else:
      return render_template('login.html', data=vdict)