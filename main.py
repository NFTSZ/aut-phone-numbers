import pandas as pd
import re
import sqlite3

path_excel = '/home/tata/projeto1/pl.xlsx'
data = pd.read_excel(path_excel)

# This standard assumes that telephone numbers have 11 digits, as in Brazil
phone_pattern = re.compile(r'\d{11}')
phone_number = []

# connect with a database
database = '/home/tata/projeto1/agenda.db'
connection = sqlite3.connect(database)

# Iterate over the phone numbers in the .xlsx and store them in the list
for indexx, line in data.iterrows():
  number = str(line['Numero de telefone'])
  matches = phone_pattern.findall(number)

  for match in matches:
    phone_number.append(match)

#remove duplicate numbers from the list
removed_dup = sorted(set(phone_number)) 

# create a table in database
with connection:
  connection.execute('''
                     CREATE TABLE IF NOT EXISTS phone_numbers (id INTEGER 
                     PRIMARY KEY, number TEXT)''')
  
  # insert the phone numbers in database
  for numbers in removed_dup:
    cursor = connection.execute('SELECT id FROM phone_numbers WHERE number = ?', 
                                (numbers,))
    existing_number = cursor.fetchone()

    if existing_number is None:
      connection.execute('INSERT INTO phone_numbers (number) VALUES (?)',
                         (numbers,))
    else:
      print(f'O numero {numbers} ja esta na tabela.')
      continue

# close the connection with the database
connection.close()

for numbers in removed_dup:
  print(numbers)
  