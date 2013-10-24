# Write functions is always a good idea because it allows us to encapsulate 
#the code which is good for better understanding, clarification, code reutilization, etc.

def create_user_profile(name, city_name, street_name):
    database = {'name':name, 'address':{'city':city_name, 'street':street_name}}
    return database



name = raw_input('Please enter the name: ')
city = raw_input("Please enter the residence's city: ")
street_name = raw_input('Please enter the street name: ')

database = create_user_profile(name, city, street_name)

print "name: ", database['name']
print "address: ", database['address']['city']
print "street name: ", database['address']['street']






