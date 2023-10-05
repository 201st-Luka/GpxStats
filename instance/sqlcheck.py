import sqlite3

conn = sqlite3.connect('db.sqlite3')
cursor = conn.cursor()

cursor.execute(f'PRAGMA table_info(users)')
column_names = [column[1] for column in cursor.fetchall()]
print(column_names)
cursor.execute('SELECT * FROM users')
rows = cursor.fetchall()
for row in rows:
    print(row)

cursor.execute(f'PRAGMA table_info(gpx_files)')
column_names = [column[1] for column in cursor.fetchall()]
print(column_names)
cursor.execute('SELECT * FROM gpx_files')
rows = cursor.fetchall()
for row in rows:
    print(row)

cursor.execute(f'PRAGMA table_info(stats)')
column_names = [column[1] for column in cursor.fetchall()]
print(column_names)
cursor.execute('SELECT * FROM stats')
rows = cursor.fetchall()
for row in rows:
    print(row)
conn.close()