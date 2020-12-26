#controllers/country.py
import config, copy, lib
from flask import render_template, redirect, session
from models.moviedb import Moviedb

class Country():
  def __init__(self):
    self.lib = lib.Lib()
    self.moviedb = Moviedb()

  def get_movie(self, label):
    vdict = copy.deepcopy(config.vdict)
    vdict['site_title'] = '​ប្រភេទ​ភាពយន្ត'
    session['page'] = 0
    session['label'] = label

    vdict['movies'] = self.moviedb.select(vdict['country_max_movie'], label=label)
    vdict['thumbs'] = self.lib.get_thumbs(vdict['movies'], 5, type='movie')

    return render_template('country.html', data=vdict)

  def load_movie(self):
    vdict = copy.deepcopy(config.vdict)
    session['page'] += 1
    vdict['movies'] = self.moviedb.select(vdict['country_max_movie'], page=session['page'], label=session['label'])
    vdict['thumbs'] = self.lib.get_thumbs(vdict['movies'], 5, type="movie")

    new_list = []
    for movie in vdict['movies']:
      new_movie = list(movie)
      new_movie[6] = movie[6].strftime('%d/%m/%Y') 
      new_movie[7] = movie[7].strftime('%H:%M:%S') 
      new_list.append(new_movie)

    vdict['movies'] = new_list
    return vdict