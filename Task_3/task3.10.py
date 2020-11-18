#Write a program which accepts a sequence of comma-separated numbers from console and
#generates a list and a tuple which contains every number in the form of string.
#Sample input: 34,67,55,33,12,98
#Expected output: [‘34’,’67’,’55’,’33’,’12’,’98’] (‘34’,’67’,’55’,’33’,’12’,’98’)


l = input("Enter comma separated numbers : ").split(",")
t = tuple(l)
print(l, type(l))
print(t, type(t))