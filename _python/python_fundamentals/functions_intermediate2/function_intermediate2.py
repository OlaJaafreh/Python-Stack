x = [ [5,2,3], [10,8,9] ] 
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]


# ###################################
# Update Values in Dictionaries and Lists


#Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].
for i in range(0,len(x),1):
    for j in range (len(x[i])):
        if x[i][j]==10:
            x[i][j]=15
            
print(x)


#Change the last_name of the first student from 'Jordan' to 'Bryant'

for i in range(0,len(students),1):
    if students[i]['last_name'] == 'Jordan':
        students[i]['last_name'] = 'Bryant' 
            
print(students)


#In the sports_directory, change 'Messi' to 'Andres'

for i in range (len(sports_directory['soccer'])):
    if sports_directory['soccer'][i] == 'Messi':
        sports_directory['soccer'][i] = 'Andres'
            
print(sports_directory)


#Change the value 20 in z to 30
if z[0]['y'] == 20:
    z[0]['y'] = 30 
            
print(z)



# ###################################
# Iterate Through a List of Dictionaries


students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

def iterateDictionary(some_list):
    for i in range(len(some_list)):
        print("First Name - " + some_list[i]['first_name'] + ", " +"Last Name - " + some_list[i]['last_name'] )

iterateDictionary(students)


# ###################################
# Get Values From a List of Dictionaries

def iterateDictionary2(key_name,some_list):
    for i in range(len(some_list)):
        if key_name == 'first_name':
            print("First Name - " + some_list[i]['first_name'] )
        if key_name == 'last_name':
            print("Last Name - " + some_list[i]['last_name'] )

iterateDictionary2('first_name', students)


# ###################################
# Iterate Through a Dictionary with List Values

dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
print("")
print(str(len(dojo['locations']))+" Locations")
for i in range (len(dojo['locations'])):    
    print(dojo['locations'][i])
print("")
print(str(len(dojo['instructors']))+" instructors")
for i in range (len(dojo['instructors'])):    
    print(dojo['instructors'][i])           

