"""
File Handling allows a program to create, read, write, and modify files.

Python provides the open() function to work with files.

Example: Writing to file
"""


with open("data.txt", "w") as f:
    f.write("Hello Python, ...ha likh diya hai python me...mil gya sukoon agya mza ....!! ")

"""
Example: Reading to a file
"""

with open("data.txt", "r") as f:
    content = f.read()

    print(content)

"""
Common file modes:


Mode    Meaning

r   Read

w   Write (overwrites existing content)

a   Append

x   Create a new file

r+  Read and write

"""