import pandas as pd
import re

path_excel = '/home/tata/projeto1/pl.xlsx'
data = pd.read_excel(path_excel)

# This standard assumes that telephone numbers have 11 digits, as in Brazil
phone_pattern = re.compile(r'\d{11}')
phone_number = []

# Iterate over the phone numbers in the .xlsx and store them in the list
for indexx, line in data.iterrows():
  number = str(line['Numero de telefone'])
  matches = phone_pattern.findall(number)

  for match in matches:
    phone_number.append(match)
    
#remove duplicate numbers from the list
remove = sorted(set(phone_number)) 

for numbers in remove:
  print(numbers, end=' ')
