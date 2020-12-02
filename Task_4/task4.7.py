#Define a function that can accept two strings as input and print the string with the maximum length
#in the console. If two strings have the same length, then the function should print both the strings line
#by line.

def compare_strings_len(s1, s2):
    if len(s1) > len(s2):
        print('String 1 is longer: ', s1)
    elif len(s1) < len(s2):
        print('String 2 is longer: ', s2)
    elif len(s1) == len(s2):
        print('String 1 and 2 length are same', s1)
        print('String 1 and 2 length are same', s2)
    else:
        print('Strings length are equal!')