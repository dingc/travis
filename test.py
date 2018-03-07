import csv

#goal is to randomly select locations based on a given list weight will help
#select certain locations more than the others - because some locations are
#more popular or yields more likes


with open('locations.csv') as locationDataFile:
	reader = csv.DictReader(locationDataFile)
	rows = [row for row in reader if row['weight'] == '5']

for row in rows:
	print(row['location'])


