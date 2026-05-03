import re

with open('App.py', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace pymysql with sqlite3
content = content.replace("import pymysql", "import sqlite3")
content = content.replace("connection = pymysql.connect(host='localhost',user='root',password='root@MySQL4admin',db='cv')", "connection = sqlite3.connect('cv.db', check_same_thread=False)")

# Replace MySQL auto_increment with sqlite3
content = content.replace("ID INT NOT NULL AUTO_INCREMENT", "ID INTEGER PRIMARY KEY AUTOINCREMENT")
content = content.replace("PRIMARY KEY (ID)", "")
# Clean up trailing comma before PRIMARY KEY
content = re.sub(r',\s*\n\s*\);', '\n);', content)

# Replace MySQL CREATE DATABASE
content = content.replace('db_sql = """CREATE DATABASE IF NOT EXISTS CV;"""\n    cursor.execute(db_sql)', '')

# Replace MySQL `%s` with sqlite3 `?` in insert query
content = content.replace('values (0,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)', 'values (NULL,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)')
content = content.replace('values (0,%s,%s,%s,%s,%s)', 'values (NULL,?,?,?,?,?)')

# Replace convert(field using utf8) with just the field, sqlite doesn't need this
content = re.sub(r'convert\((.*?) using utf8\)', r'\1', content)

with open('App.py', 'w', encoding='utf-8') as f:
    f.write(content)

print("App.py updated for sqlite3")
