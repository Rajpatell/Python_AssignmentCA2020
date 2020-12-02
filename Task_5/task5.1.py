#Write a program in Python to allow the error of syntax to be handled using exception handling.
#HINT: Use SyntaxError


try:
    x = "Raj"
    a = eval("My name is " + x)
    print(a)
except SyntaxError:
    print("You have Syntax Error")
finally:
    print("Done")