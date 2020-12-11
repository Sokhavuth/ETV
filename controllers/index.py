#controllers/index.py
import config
from bottle import Bottle, template, static_file
 
class Index(Bottle):
    def __init__(self):
        super(Index, self).__init__()
        self.route('/static/images/<filename>', callback=self.loadImage)
        self.route('/static/styles/<filename>', callback=self.loadStyle)
        self.route('/static/scripts/<filename>', callback=self.loadScript)
        self.route('/static/fonts/<filename>', callback=self.loadFont)
 
        self.route('/', callback=self.index)
 
    def loadImage(self, filename):
        return static_file(filename, root='./public/images')
 
    def loadStyle(self, filename):
        return static_file(filename, root='./public/css')
 
    def loadScript(self, filename):
        return static_file(filename, root='./public/js')
 
    def loadFont(self, filename):
        return static_file(filename, root='./public/fonts')
 
    def index(self):
        return template('index', data=config.vdict)