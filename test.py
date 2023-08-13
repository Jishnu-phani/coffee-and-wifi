# import csv
# import pandas
#
# data = pandas.read_csv('cafe-data.csv')
#
# print(data)

import csv
file = open('cafe-data.csv', encoding="utf-8")
reader = csv.reader(file)
data = [line for line in reader]
print(data)
print(data[0][0])