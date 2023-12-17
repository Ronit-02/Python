# Tuples 
# Immutable: value can't be changed

# Syntax

from unittest import result


print()
a = (1,2,3,4)
print(a)

fullname = ('Ronit', 'Khatri')


# Use in Functions

print()
def convert_seconds(seconds):
    hours = seconds // 3600
    minutes = (seconds - hours*3600) // 60
    remaining_seconds = (seconds - hours*3600 - minutes*60)
    return hours, minutes, remaining_seconds   # return tuple

result = convert_seconds(5600)
print(result)   # tuple

hours, minutes, seconds = result  # unpacking tuple
print(hours, minutes, seconds)