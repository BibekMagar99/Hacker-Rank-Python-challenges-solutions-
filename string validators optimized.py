str = input()
print(any(c.isalnum()  for c in str))
print(any(c.isalpha() for c in str))
print(any(c.isdigit() for c in str))
print(any(c.islower() for c in str))
print(any(c.isupper() for c in str))

#any() The any() function returns True if any item in an iterable are true,
# otherwise it returns False.
#If the iterable object is empty, the any() function will return False.
