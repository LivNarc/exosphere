
import csv

def convert_to_html(dictionary, indent=0):
 p=[]
 p.append('<ul>\n')
 for k,v in dictionary.iteritems():
 		if isinstance(v, dict):
 	  		p.append('<li>'+ str(k) + ':')
 	        	p.append(convert_to_html(v))
 	        	p.append('</li>')
     		else:
 	        	p.append('<li>'+ str(k) + ':'+ str(v) + '</li>')
 			p.append('</ul>\n')
 return '\n'.join(p)

def printplain(products):
	print products
		
def printhtml(products):
	html_format_list = convert_to_html(products) 
	print html_format_list
	return html_format_list


products ={}

user_file = raw_input('which file would you like to open:\n\t')
form = raw_input('which format would you like:\n\t 1 for HTML\n\t 2 for Plain\n\t')

with open(user_file,'rb') as csvfile:
	report = csv.reader(csvfile, delimiter =';')
	for row in report: 
		products[row[0]] = {'qty':row[3], 'revenue':row[2]}


int_form= int(form)
if int_form is 1:
	html_format_list = printhtml (products)
elif int_form is 2:
	printplain (products)
else:
	print 'invalid msg'

file = open('index.html', 'w')
file.write (html_format_list) 