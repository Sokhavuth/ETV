#controllers/movie.py
import config, copy, lib
from flask import render_template, redirect
from models.moviedb import Moviedb
from models.userdb import Userdb

class Movie():
  def __init__(self):
    self.lib = lib.Lib()
    self.userdb = Userdb()
    self.moviedb = Moviedb()

  def get_movie(self, id):
    vdict = copy.deepcopy(config.vdict)
    vdict['site_title'] = '​ភាពយន្ត​ទោល'

    vdict['movies'] = self.moviedb.select(vdict['random_max_post'], random=id)
    vdict['thumbs'] = self.lib.get_thumbs(vdict['movies'], 5, type='movie')
    vdict['movie'] = self.moviedb.select(id=id)
    date = (vdict['movie'][6]).strftime('%d/%m/%Y')
    time = (vdict['movie'][7]).strftime('%H:%M:%S')
    vdict['datetime'] = (date, time)
    vdict['author'] = self.userdb.select(username=vdict['movie'][8])

    return render_template('movie.html', data=vdict)
