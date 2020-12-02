#Write a program in Python to allow the user to open a file by using the argv module. If the
#entered name is incorrect throw an exception and ask them to enter the name again. Make sure
#to use read only mode.

import sys
def file_open():
    try:
        name = sys.argv[1]
        my_file = open(name, 'r')
        my_str = my_file.read()
        print(my_str)
        my_file.close()
    except FileNotFoundError:
        print("file name incorrect! enter again")

file_open()