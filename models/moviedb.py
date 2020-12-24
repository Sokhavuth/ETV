#models/moviedb.py
import os, psycopg2

class Moviedb():
  def __init__(self):
    self.create_table()

  def set_conection(self):
    if 'DYNO' in os.environ:
      DATABASE_URL = os.environ['DATABASE_URL']
      self.conn = psycopg2.connect(DATABASE_URL, sslmode='require')
      self.cursor = self.conn.cursor()
    else: 
      self.conn = psycopg2.connect(
        database="postgres", 
        user="postgres", 
        password="sokhavuth", 
        host="localhost", 
        port="5432"
      )

      self.cursor = self.conn.cursor()

  def create_table(self):
    self.set_conection()
    
    SQL = '''CREATE TABLE IF NOT EXISTS MOVIES(
      ID TEXT,
      VID TEXT,
      TYPE TEXT,
      TITLE TEXT,
      COUNTRY TEXT,
      CONTENT TEXT,
      CDATE DATE,
      CTIME TIME,
      AUTHOR TEXT
    )'''

    self.cursor.execute(SQL)
    self.conn.commit()
    self.conn.close() 

  def insert(self, *movie):
    self.set_conection()

    self.cursor.execute("INSERT INTO MOVIES (ID, VID, TYPE, TITLE, COUNTRY, CONTENT, CDATE, CTIME, AUTHOR) VALUES %s ", (movie,))
  
    self.conn.commit()
    self.conn.close()

  def select(self, amount=5, id='', page=0, random=False, type=None):
    self.set_conection()

    if id:
      SQL = "SELECT * FROM MOVIES WHERE ID=%s"
      self.cursor.execute(SQL, (id,))
      result = self.cursor.fetchone()
    elif page:
      SQL = "SELECT * FROM MOVIES ORDER BY CDATE DESC, CTIME DESC OFFSET %s ROWS FETCH NEXT %s ROWS ONLY"
      self.cursor.execute(SQL, (amount*page, amount))
      result = self.cursor.fetchall()
    elif random:
      SQL = "SELECT	* FROM MOVIES WHERE ID != %s ORDER BY RANDOM() LIMIT %s"
      self.cursor.execute(SQL, (random, amount))
      result = self.cursor.fetchall()
    elif type:
      SQL = "SELECT * FROM MOVIES WHERE TYPE = %S ORDER BY CDATE DESC, CTIME DESC LIMIT %s"
      self.cursor.execute(SQL, (type, amount))
      result = self.cursor.fetchall()
    else:
      SQL = "SELECT * FROM MOVIES ORDER BY CDATE DESC, CTIME DESC LIMIT %s"
      self.cursor.execute(SQL, (amount,))
      result = self.cursor.fetchall()

    self.conn.close()
    return result

  def delete(self, id):
    self.set_conection()

    SQL = "DELETE FROM MOVIES WHERE ID = %s"
    self.cursor.execute(SQL, (id,))

    self.conn.commit()
    self.conn.close()

  def update(self, *movie):
    self.set_conection()

    sql = "UPDATE MOVIES SET VID = %s, TYPE = %s, TITLE = %s, COUNTRY = %s, CONTENT = %s, CDATE = %s, CTIME = %s, AUTHOR = %s WHERE ID = %s"
    self.cursor.execute(sql, movie)

    self.conn.commit()
    self.conn.close()

  def search(self, query):
    self.set_conection()
  
    sql = "SELECT * from USERS WHERE"
    sql += " EMAIL LIKE '%"+query+"%'"
    sql += " OR CONTENT LIKE '%"+query+"%'"
    sql += " ORDER BY CATDATE DESC, CATTIME DESC LIMIT 20"

    self.cursor.execute(sql)
    
    result = self.cursor.fetchall()
    return result