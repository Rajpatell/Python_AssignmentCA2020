#Write a program in Python using generators to reverse the string.
#Input String = “Consultadd Training”



def gen(s):
    for k in range(len(s), 0, -1):
        yield k

s = "Consultadd Training"
s1 = ""

for i in gen(s):
    s1 = s1+(s[i - 1])

print("Reverse string is : ", s1)