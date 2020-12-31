#controllers/series.py
import config, copy, lib
from flask import render_template, redirect
from models.userdb import Userdb
from models.seriesdb import Seriesdb

class Series():
  def __init__(self):
    self.lib = lib.Lib()
    self.userdb = Userdb()
    self.seriesdb = Seriesdb()

  def get_series(self, id):
    vdict = copy.deepcopy(config.vdict)
    vdict['site_title'] = '​ភាពយន្ត​ភាគ'

    vdict['series'] = self.seriesdb.select(vdict['random_max_movie'], random=id)
    vdict['thumbs'] = self.lib.get_thumbs(vdict['series'], 4, type='movie')
    vdict['serie'] = self.seriesdb.select(id=id)
    date = (vdict['serie'][5]).strftime('%d/%m/%Y')
    time = (vdict['serie'][6]).strftime('%H:%M:%S')
    vdict['datetime'] = (date, time)
    vdict['author'] = self.userdb.select(username=vdict['serie'][7])

    return render_template('series.html', data=vdict)
