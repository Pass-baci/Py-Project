import mysql.connector

db = mysql.connector.connect(host='127.0.0.1', port=3306, user='root', password='root')
db_cursor = db.cursor()

db_cursor.execute("SHOW DATABASES")
database_name = 'my_database'
database_exist = False
for i in db_cursor:
    if database_name in i:
        database_exist = True
if not database_exist:
    db_cursor.execute("CREATE DATABASE my_database")

db_cursor.execute(f'USE {database_name}')

db_cursor.execute("SHOW TABLES")
table_name = 'customers'
table_exist = False
for i in db_cursor:
    if table_name in i:
        table_exist = True
if not table_exist:
    db_cursor.execute(f"CREATE TABLE {table_name} (name VARCHAR(255), address VARCHAR(255))")

db_cursor.execute(f'DROP TABLE {table_name}')

db_cursor.execute(f'CREATE TABLE {table_name} (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))')

sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("John", "Highway 21")
db_cursor.execute(sql, val)
db.commit()
print(db_cursor.lastrowid)

sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = [
  ('Peter', 'Lowstreet 4'),
  ('Amy', 'Apple st 652'),
  ('Hannah', 'Mountain 21'),
  ('Michael', 'Valley 345'),
  ('Sandy', 'Ocean blvd 2'),
  ('Betty', 'Green Grass 1'),
  ('Richard', 'Sky st 331'),
  ('Susan', 'One way 98'),
  ('Vicky', 'Yellow Garden 2'),
  ('Ben', 'Park Lane 38'),
  ('William', 'Central st 954'),
  ('Chuck', 'Main Road 989'),
  ('Viola', 'Sideway 1633')
]
db_cursor.executemany(sql, val)
db.commit()

db_cursor.execute(f'SELECT * FROM {table_name}')
result = db_cursor.fetchall()
for value in result:
    print(value, type(value))

db_cursor.execute(f'SELECT name FROM {table_name}')
result = db_cursor.fetchall()
for value in result:
    print(value, type(value))

db_cursor.execute(f'SELECT name FROM {table_name} LIMIT 1')
result = db_cursor.fetchone()
print(result)

db_cursor.execute(f"SELECT * FROM {table_name} WHERE address LIKE '%way%'")
result = db_cursor.fetchall()
for value in result:
    print(value, type(value))

sql = f"SELECT * FROM {table_name} WHERE address = %s"
adr = ("Yellow Garden 2", )
db_cursor.execute(sql, adr)
result = db_cursor.fetchall()
for value in result:
    print(value, type(value))



