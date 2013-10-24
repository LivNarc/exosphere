
import csv

products ={}

user_file = raw_input('which file would you like to open:\n\t')
form = raw_input('which format would you like:n\t\'HTML'n\t\'Plain')

if form is 'HTML':
	print 'HTML Report Here'
elif 'Plain' is:
	print 'Plain Report Here'
else:
	print 'invalid msg

with open(user_file,'rb') as csvfile:
	report = csv.reader(csvfile, delimiter =';')
	for row in report: 
		products[row[0]] = {'qty':row[3], 'revenue':row[2]}
print products

