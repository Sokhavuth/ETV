#public/setup.py
from bottle import route, static_file
  
@route('/static/scripts/<filename>')    
def server_static(filename):
  return static_file(filename, root='./public/js')

@route('/static/scripts/ckeditor/<filename>')    
def server_static(filename):
  return static_file(filename, root='./public/js/ckeditor')
   
@route('/static/styles/<filename>')    
def server_static(filename):
  return static_file(filename, root='./public/css')
   
@route('/static/images/<filename>')    
def server_static(filename):
  return static_file(filename, root='./public/images')

@route('/static/images/uploads/<filename>')    
def server_static(filename):
  return static_file(filename, root='./public/images/uploads')
   
@route('/static/fonts/<filename>')    
def server_static(filename):
  return static_file(filename, root='./public/fonts')