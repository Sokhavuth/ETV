#controllers/home.py
import config, copy, lib
from flask import render_template, redirect
from models.moviedb import Moviedb
from models.seriesdb import Seriesdb

class Home():
  def __init__(self):
    self.lib = lib.Lib()
    self.moviedb = Moviedb()
    self.seriesdb = Seriesdb()

  def get_youtube(self):
    self.vdict = copy.deepcopy(config.vdict)
    self.get_movie()
    self.get_series()
    return render_template('index.html', data=self.vdict)

  def get_movie(self):
    self.vdict['movies'] = self.moviedb.select(self.vdict['home_max_movie'])
    self.vdict['thumbs'] = self.lib.get_thumbs(self.vdict['movies'], 5, type='movie')

  def get_series(self):
    self.vdict['series'] = self.seriesdb.select(self.vdict['home_max_movie'])
    self.vdict['series-thumbs'] = self.lib.get_thumbs(self.vdict['series'], 4, type='movie')
