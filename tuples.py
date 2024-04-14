integers = (20,60,80,10,100,50)
print(integers[3])
print(integers[1:4])

fruits = ("Sandthra", "Pawpaw", "Oranges", "Mangoes")
print(fruits[2])

#lengthoftuple
print(len(fruits))

#number of times an element has appread in a list
print(fruits.count('Oranges'))

#sorting in ascending order
print(sorted(fruits))

#add and delete an item 
print(fruits)
tupletolist = list(fruits)
print(tupletolist)
print(tupletolist.pop())
tupletolist.append("Pineapples")
print(tupletolist)

tupletolist.remove("Pawpaw")
print(tupletolist)
