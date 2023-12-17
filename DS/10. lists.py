# Features
# Mutable (can edit elements)
# Heterogenous (support all data types)


name = ["ronit","samarth","shrishti","prateek"]
print(name)

name[1] = "sonal"
del name[0]
print(name)


# List Comprehension, new_list = [expression | for item in list | if condition]

print()
pow2 = [2**x for x in range(11)]
print(pow2)

even = [x for x in range(10) if x%2 == 0]
print(even)

languages = ["Python", "C++", "Java", "Ruby"]
lengths = [len(language) for language in languages]
print(lengths)


# List Methods

print()
a = [1,3,4]
a.insert(1,2)   # insert(idx, value)
a.append(1)
a.sort()
print(a)
a.clear()

print()
b = [1,2,3,4,5]
b.pop()
print(b)

print() 
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)  # can add any iterable object(tuples, sets, dictionaries)
print(thislist)


# List Functions

print()
c = [1,2,3,4,5]
print(len(c))
print(max(c))
print(min(c))


# Iterating over list

print()
ages = [23, 25, 18]
for age in ages:
    print(age)

print()
winners = ["Rohan","Yash","Harshit"]
for index, people in enumerate(winners):
    print("{} - {}".format(index, people))