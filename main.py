# Section 227 - Reading CSV Data into Python #1 Challenge
# with open("weather_data.csv", "r") as f:
#     list = f.readlines()
#     print(list)

# Section 227 - Reading CSV Data into Python Challenge - After Lecture
# import csv
#
# with open("weather_data.csv", "r") as f:
#     data = csv.reader(f)
#     for row in data:
#         print(row)

# Section 227a - Reading CSV Data into Python Challenge #2
# import csv
#
# with open("weather_data.csv", "r") as f:
#     data = csv.reader(f)
#     temperature = []
#     for row in data:
#         if row[1] == 'temp':
#             pass
#         else:
#             temperature.append(int(row[1]))
#     print(temperature)

# Section 227b - Pandas
import pandas as pd

data = pd.read_csv('weather_data.csv')
print(data['temp'])