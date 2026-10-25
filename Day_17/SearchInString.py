# Searching in string
# find() -> This method is used to search for a substring or character in a given string.
# It returns the index of the first occurrence, or -1 if not found.
# index() -> This method also searches for a substring or character and returns its index.
# It raises a ValueError if the value is not found.

text = input("Enter a string: ").lower()
search = input("Enter the value to search: ").lower()

print("Using find():")
index = text.find(search)

if index != -1:
    print(f"'{search}' found at index {index}")
else:
    print(f"'{search}' not found in the string")

print("\nUsing index():")
try:
    pos = text.index(search)
    print(f"'{search}' found at index {pos}")
except ValueError:
    print(f"'{search}' not found in the string")

