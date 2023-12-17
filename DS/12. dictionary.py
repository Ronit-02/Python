
result = {
	'Ronit': 34,
	'Samarth': 45,
	'Yash': 81
}
result['Anuj'] = 99
result.update({"Naman": 56})
print(result)


# Traversing

print()
for i in result:
	print(i, "->",result[i])

print()
for name, marks in result.items():
	print("{} acheived {} marks.".format(name, marks))


# Dictionary Methods

print()
print(result.keys())
print(result.values())