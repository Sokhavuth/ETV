#controllers/dashboard/signup.py
import config, copy
from models.userdb import Userdb

class Signup():
  def __init__(self):
    self.userdb = Userdb()


  def signup(self):
    vdict = copy.deepcopy(config.vdict)
    vdict['siteTitle'] = "ទំព័រ​ចុះ​ឈ្មោះ"

    
      
    return "Signup"

