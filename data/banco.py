import mysql.connector
from mysql.connector import errorcode

print("Connecting...")
try:
      conn = mysql.connector.connect(
            host='127.0.0.1',
            user='root',
            password='admin'
      )
except mysql.connector.Error as err:
      if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print('There is something wrong with the username or password!')
      else:
            print(err)

cursor = conn.cursor()

cursor.execute("DROP DATABASE IF EXISTS `projetoxp`;")

cursor.execute("CREATE DATABASE `projetoxp`;")

cursor.execute("USE `projetoxp`;")

# Creating Tables
TABLES = {}
TABLES['Students'] = ('''
      CREATE TABLE `students` (
      `id` int(11) NOT NULL AUTO_INCREMENT,
      `name` varchar(100) NOT NULL,
      `email` varchar(50) NOT NULL,
      `phone` varchar(15) NOT NULL,
      PRIMARY KEY (`id`)
      ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;''')

TABLES['Users'] = ('''
      CREATE TABLE `users` (
      `name` varchar(20) NOT NULL,
      `nickname` varchar(10) NOT NULL,
      `keyword` varchar(100) NOT NULL,
      PRIMARY KEY (`nickname`)
      ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;''')

for table_name in TABLES:
      table_sql = TABLES[table_name]
      try:
            print('Creating {}:'.format(table_name), end=' ')
            cursor.execute(table_sql)
      except mysql.connector.Error as err:
            if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                  print('Already Exists!')
            else:
                  print(err.msg)
      else:
            print('OK!')


# Inserting Users
user_sql = 'INSERT INTO users (name, nickname, keyword) VALUES (%s, %s, %s)'
users = [
      ("Henrique Morais", "rikemorais", "alohomora"),
      ("Paty Morais", "patymorais", "patinha")
]
cursor.executemany(user_sql, users)

cursor.execute('select * from projetoxp.users')
print(' -------------  Users  -------------')
for user in cursor.fetchall():
    print(user[1])

# Inserting Students
students_sql = 'INSERT INTO students (name, email, phone) VALUES (%s, %s, %s)'
students = [
      ("Henrique Morais", "rikeaju@hotmail.com", "5579991124671"),
      ("Paty Morais", "patymorais@hotmail.com", "5579998555140")
]
cursor.executemany(students_sql, students)

cursor.execute('select * from projetoxp.students')
print(' -------------  Students  -------------')
for student in cursor.fetchall():
    print(student[1])

# Committing if nothing takes effect
conn.commit()

cursor.close()
conn.close()