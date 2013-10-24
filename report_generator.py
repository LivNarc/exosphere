import csv

products ={}

with open('branch1.csv','rb') as csvfile:
	report = csv.reader(csvfile, delimiter =';')
	for row in report: 
		products[row[0]] = {'qty':row[2], 'revenue':row[3]}
print products


option = raw_input('please choose an option:\n\t 1 for hello world\n\t 2 for hola mundo\n\t')

int_option= int(option)
if int_option is 1:
	print 'welcome'
elif int_option is 2:
	print 'bienvenidos'
else:
	print 'invalid msg

--------

import csv

products ={}

user_file = raw_input('which file would you like to open:\n\t')

with open(user_file,'rb') as csvfile:
	report = csv.reader(csvfile, delimiter =';')
	for row in report: 
		products[row[0]] = {'qty':row[2], 'revenue':row[3]}
