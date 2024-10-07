# Create a list:
list1=[1,2,3,4,5,6]
print("The orignal list is:",list1)
# Add the element in list:
list1.append(7)
print("Add an element to the list:",list1)
#Remove the element in list:
list1.remove(4)
print("An element was removed from the list",list1)
#Modifying an element in the list:
list1[2]=10
print("An element was modifying in the list", list1)

print('\n')

# Create a dictonary:
dict1={'a':'Mohit','b':'Neeraj','c':'Sandeep','d':'Rohit'}
print("The orignal dictonary is:",dict1)
#Add the new element in dictonary:
dict1["d"]="Rakesh"
print("Add an new element to the dictonary", dict1)
#Remove the element in dictonary:
dict1.pop('b')
print("An element was remove from the dictonary", dict1)

#Modifying the element in dictonary:
dict1["c"]="Vishal"
print("An element was modifying in the dictonary",dict1)

print('\n')

# create a set:
set1={1,2,3,5,6}
print("The orignal set is:", set1)
#Add a new element in set:
set1.add(4)
print("Add an new element to the set", set1)
#Remove a element in set:
set1.remove(3)
print("An element was remove from the set",set1)
# Modifying the element in set:
set1.discard(5)
set1.add(8)
print("An element was modifying in  set", set1)