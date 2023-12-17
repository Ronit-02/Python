# Break

for i in range(1, 10, 2):
	if i > 6:
		break
	print(i, end=" ")
print()


# Continue

print()
for i in range(5):
	if i == 2:      
		continue
	print(f"{i} -> {i*2}")