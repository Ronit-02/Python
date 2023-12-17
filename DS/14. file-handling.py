# Reading: First Way

print('First way: ')
f = open('data/data1.txt', 'r')
for line in f:
	print(line, end="")

f.close()


# Second Way

print()
print('\nSecond way: ')
with open('data/data1.txt', 'r') as f:
	print(f.read(9), end="")
	f.seek(15)
	print(f.read(19))

f.close()


# Writing

names = ['Ronit', 'Yash', 'Anuj']

with open('data/write1.txt', 'w') as f:
	f.write('Hello \n')
	f.writelines(names)

f.close()


with open('data/write1.txt', 'r') as f:
	print(f.read())

f.close()