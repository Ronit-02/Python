# writing

names = ['Ronit', 'Yash', 'Anuj']

with open('data/write1.txt', 'w') as f:
	f.write('Hello \n')
	f.writelines(names)

f.close()


# reading

with open('data/write1.txt', 'r') as f:
	print(f.read())

f.close()