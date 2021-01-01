#controllers/dashboard/movie.py
import config, copy, lib, datetime, uuid, json
from flask import render_template, session, request, redirect
from models.seriesdb import Seriesdb

class Series():
  def __init__(self):
    self.lib = lib.Lib()
    self.seriesdb = Seriesdb()

  def get_post(self):
    vdict = copy.deepcopy(config.vdict)
    vdict['site_title'] = "ទំព័រ​ភាពយន្តភាគ"
    vdict['datetime'] = self.lib.get_timezone()
    session['page'] = 0

    if (request.method == "POST") and ('logged-in' in session):
      title = request.form['ftitle']
      content = request.form['fcontent']
      playlist = request.form['fplaylist']
      country = request.form['fcountry']
      date = request.form['fdate']
      time = request.form['ftime']
      author = session['logged-in']
      ending = request.form['fend']
      edit_id = request.form['fedit-id']
      print(edit_id)
      try:
        date = datetime.datetime.strptime(date, "%d/%m/%Y")
      except ValueError:
        vdict['message'] = 'ទំរង់​កាលបរិច្ឆេទ​មិន​ត្រឹមត្រូវ!'
        return render_template('dashboard/series.html', data=vdict)

      try:
        time = datetime.datetime.strptime(time, "%H:%M:%S")
      except ValueError:
        vdict['message'] = 'ទំរង់​ពេល​វេលា​មិន​ត្រឹមត្រូវ!'
        return render_template('dashboard/series.html', data=vdict)

      if edit_id:
        self.seriesdb.update(playlist, title, country, content, date, time, author, ending, edit_id)
      else:
        id = str(uuid.uuid4().int)
        self.seriesdb.insert(id, playlist, title, country, content, date, time, author, ending)

      vdict['series'] = self.seriesdb.select(vdict['dashboard_max_post'])
      vdict['count'] = self.seriesdb.count()
      vdict['thumbs'] = self.lib.get_thumbs(vdict['series'], 4, type='movie')
      return render_template('dashboard/series.html', data=vdict)

    elif 'logged-in' in session:
      vdict['series'] = self.seriesdb.select(vdict['dashboard_max_post'])
      vdict['count'] = self.seriesdb.count()
      vdict['thumbs'] = self.lib.get_thumbs(vdict['series'], 4, type='movie')
      return render_template('dashboard/series.html', data=vdict)
    else:
      return redirect('/login/')

  def edit(self, id):
    vdict = copy.deepcopy(config.vdict)
    vdict['site_title'] = 'កែតំរូវ​ភាពយន្ត​ភាគ'
    vdict['edit-id'] = id

    if 'logged-in' in session:
      vdict['series'] = self.seriesdb.select(vdict['dashboard_max_post'])
      vdict['count'] = self.seriesdb.count()
      vdict['thumbs'] = self.lib.get_thumbs(vdict['series'], 4, type='movie')
      vdict['serie'] = self.seriesdb.select(id=id)
      date = (vdict['serie'][5]).strftime('%d/%m/%Y')
      time = (vdict['serie'][6]).strftime('%H:%M:%S')
      vdict['datetime'] = (date, time)

      return render_template('dashboard/series.html', data=vdict)

    return redirect('/login/')

  def delete(self, id):
    self.seriesdb.delete(id)
    return redirect('/dashboard/series/')

  def load(self):
    if 'logged-in' in session:
      vdict = copy.deepcopy(config.vdict)
      session['page'] += 1
      vdict['series'] = self.seriesdb.select(vdict['dashboard_max_post'], page=session['page'])
      vdict['thumbs'] = self.lib.get_thumbs(vdict['series'], 4, type="movie")

      new_list = []
      for serie in vdict['series']:
        new_serie = list(serie)
        new_serie[5] = serie[5].strftime('%d/%m/%Y') 
        new_serie[6] = serie[6].strftime('%H:%M:%S') 
        new_list.append(new_serie)

      vdict['series'] = new_list
      return vdict
    else:
      return render_template('login.html', data=vdict)