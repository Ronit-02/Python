# Features:
# Immutable (can't be modified)


# Template Strings (can write in multiple lines)

from pyexpat.errors import messages


name = '''Ronit 
Khatri
'''
print(name)


# Negative Indexing

print()
print("First letter is", name[0])
print("Last letter is", name[-2])   # last letter is '\n'


# Slicing, str[start : end : gap/direction]

print()
s = "abcd"
print(s[1:4])
print(s[:4])
print("String reverse:", s[::-1])


# Modify String (copy and modify)
 
print()
message = "a kong string with silly typo"
idx = message.index("kong")
new_message = message[:idx] + "l" + message[idx+1:]
print(message)
print(new_message)


# Arithmetic Operation

print()
a = "ab"
b = "cd"
print("Addition: ",a+b)
print("Multiplication: ",a*2)


# String Methods

s = "This is random Sub String"
print()
print('string:', s)
print('s.isalpha:', s.isalpha())
print('s.islower:', s.islower())
print('s.upper:', s.upper())
print('s.lower:', s.lower())
print('count no of s:', s.count("e"))
print('ends with \'String\'?', s.endswith("String"))

s = '  a  '
print('a.strip', a.strip())  # remove all extra white-space, tabs, new linen chars
print('a.lstrip:', a.lstrip())  # remove left side spaces
print('a.lstrip:', a.rstrip())  # remove right side spaces


# String Join

print()
str1 = " ".join(["this","is","a","phrase","joined","with","spaces"])
print(str1)
str2 = "...".join(["this","is","a","phrase","joined","with","triple","dots"])
print(str2)


# String Split (inverse of join)

print()
phrase = "This is a one liner phrase"
phrase_list = phrase.split()
print(phrase_list)


# String Formatting

print()
name = "Manny"
number = len(name * 3)
print("Hello {}, your lucky number is {}".format(name, number))

print()
price = 7.5
print("With tax, price is {price:.2f}Rs".format(price=price*1.5))