#models/seriesdb.py
import os, psycopg2

class Seriesdb():
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
    
    SQL = '''CREATE TABLE IF NOT EXISTS SERIES(
      ID TEXT,
      VIDTYPE TEXT,
      TITLE TEXT,
      COUNTRY TEXT,
      CONTENT TEXT,
      CDATE DATE,
      CTIME TIME,
      AUTHOR TEXT,
      ENDING TEXT
    )'''

    self.cursor.execute(SQL)
    self.conn.commit()
    self.conn.close() 

  def insert(self, *series):
    self.set_conection()

    self.cursor.execute("INSERT INTO SERIES (ID, VIDTYPE, TITLE, COUNTRY, CONTENT, CDATE, CTIME, AUTHOR, ENDING) VALUES %s ", (series,))
  
    self.conn.commit()
    self.conn.close()

  def select(self, amount=5, id='', page=0, random=False, type=None, label=''):
    self.set_conection()

    if id:
      SQL = "SELECT * FROM SERIES WHERE ID=%s"
      self.cursor.execute(SQL, (id,))
      result = self.cursor.fetchone()
    elif page and label:
      if label == "all":
        SQL = "SELECT * FROM SERIES ORDER BY CDATE DESC, CTIME DESC OFFSET %s ROWS FETCH NEXT %s ROWS ONLY"
      else:
        SQL = "SELECT * FROM SERIES WHERE COUNTRY = '"+label+"' ORDER BY CDATE DESC, CTIME DESC OFFSET %s ROWS FETCH NEXT %s ROWS ONLY"

      self.cursor.execute(SQL, (amount*page, amount))
      result = self.cursor.fetchall()
    elif page:
      SQL = "SELECT * FROM SERIES ORDER BY CDATE DESC, CTIME DESC OFFSET %s ROWS FETCH NEXT %s ROWS ONLY"
      self.cursor.execute(SQL, (amount*page, amount))
      result = self.cursor.fetchall()
    elif random:
      SQL = "SELECT	* FROM SERIES WHERE ID != %s ORDER BY RANDOM() LIMIT %s"
      self.cursor.execute(SQL, (random, amount))
      result = self.cursor.fetchall()
    elif type:
      SQL = "SELECT * FROM MOVIES WHERE TYPE = %S ORDER BY CDATE DESC, CTIME DESC LIMIT %s"
      self.cursor.execute(SQL, (type, amount))
      result = self.cursor.fetchall()
    elif label:
      if label == 'all':
        SQL = "SELECT * FROM SERIES ORDER BY CDATE DESC, CTIME DESC LIMIT %s"
      else:
        SQL = "SELECT * FROM SERIES WHERE COUNTRY = '"+label+"' ORDER BY CDATE DESC, CTIME DESC LIMIT %s"

      self.cursor.execute(SQL, (amount,))
      result = self.cursor.fetchall()
    else:
      SQL = "SELECT * FROM SERIES ORDER BY CDATE DESC, CTIME DESC LIMIT %s"
      self.cursor.execute(SQL, (amount,))
      result = self.cursor.fetchall()

    self.conn.close()
    return result

  def delete(self, id):
    self.set_conection()

    SQL = "DELETE FROM SERIES WHERE ID = %s"
    self.cursor.execute(SQL, (id,))

    self.conn.commit()
    self.conn.close()

  def update(self, *series):
    self.set_conection()

    sql = "UPDATE SERIES SET VIDTYPE = %s, TITLE = %s, COUNTRY = %s, CONTENT = %s, CDATE = %s, CTIME = %s, AUTHOR = %s, ENDING = %s WHERE ID = %s"
    self.cursor.execute(sql, series)

    self.conn.commit()
    self.conn.close()

  def count(self):
    self.set_conection()

    sql = "SELECT COUNT(*) FROM SERIES"
    self.cursor.execute(sql)
    result = self.cursor.fetchone()

    self.conn.close()
    return result[0]

  def search(self, query):
    self.set_conection()
  
    sql = "SELECT * from USERS WHERE"
    sql += " EMAIL LIKE '%"+query+"%'"
    sql += " OR CONTENT LIKE '%"+query+"%'"
    sql += " ORDER BY CATDATE DESC, CATTIME DESC LIMIT 20"

    self.cursor.execute(sql)
    
    result = self.cursor.fetchall()
    return result