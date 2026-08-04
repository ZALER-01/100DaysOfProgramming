#List always opens with a Square Braces

States_of_india= ['Bihar', 'Uttarakhand','Chennai','Mumbai','Bangalore']
#[                    0           1           2         3           4
#[                   -5           -4          -3         -2           -1
#Accessing a list by using index
# indexes starts with 0

print(States_of_india[0])
print(States_of_india[1])
print(States_of_india[-2])
#We can use append to add more data to list

States_of_india.append('Shimla')
print(States_of_india)

States_of_india.remove('Shimla') #we can drop any item from list
print(States_of_india)
States_of_india.sort()
print(States_of_india)








