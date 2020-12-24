#controllers/home.py
import config, copy, lib
from flask import render_template, redirect
from models.moviedb import Moviedb

class Home():
  def __init__(self):
    self.lib = lib.Lib()
    self.moviedb = Moviedb()

  def get_youtube(self):
    self.vdict = copy.deepcopy(config.vdict)
    self.get_movie()
    return render_template('index.html', data=self.vdict)

  def get_movie(self, type=None):
    self.vdict['movies'] = self.moviedb.select(self.vdict['home_max_movie'])
    self.vdict['thumbs'] = self.lib.get_thumbs(self.vdict['movies'], 5, type='movie')
