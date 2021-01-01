#controllers/country_series.py
import config, copy, lib
from flask import render_template, redirect, session
from models.seriesdb import Seriesdb

class Country_series():
  def __init__(self):
    self.lib = lib.Lib()
    self.seriesdb = Seriesdb()

  def get_series(self, label):
    vdict = copy.deepcopy(config.vdict)
    vdict['site_title'] = '​ប្រភេទ​ភាពយន្ត'
    session['page'] = 0
    session['label'] = label

    vdict['series'] = self.seriesdb.select(vdict['country_max_movie'], label=label)
    vdict['thumbs'] = self.lib.get_thumbs(vdict['series'], 4, type='movie')

    return render_template('country_series.html', data=vdict)

  def load_series(self):
    vdict = copy.deepcopy(config.vdict)
    session['page'] += 1
    vdict['series'] = self.seriesdb.select(vdict['country_max_movie'], page=session['page'], label=session['label'])
    vdict['thumbs'] = self.lib.get_thumbs(vdict['series'], 4, type="movie")

    new_list = []
    for serie in vdict['series']:
      new_serie = list(serie)
      new_serie[5] = serie[5].strftime('%d/%m/%Y') 
      new_serie[6] = serie[6].strftime('%H:%M:%S') 
      new_list.append(new_serie)

    vdict['series'] = new_list
    return vdict