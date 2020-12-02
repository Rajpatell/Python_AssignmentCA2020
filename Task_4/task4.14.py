#Write a program in Python to find the values which are not divisible by 3 but are a multiple of 7.
#Make sure to use only higher order functions.

def n_list(l):
    new = list(filter(lambda x: x%3 != 0 and x%7 == 0, 1))
    print(new)