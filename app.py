import eel
import sqlite3

conn = sqlite3.connect("userdata.db")

cursor = conn.cursor()

cursor.execute(
  '''CREATE TABLE userdata(
      file_location text,
      web_url text,
      image_path text,
      image blob
  )'''
)

conn.commit()

# eel.init("web") 
# eel.start("index.html") 