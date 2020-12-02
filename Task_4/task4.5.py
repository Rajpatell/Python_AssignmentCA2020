# Write a program that accepts sequence of lines as input and 
#prints the lines after making all characters in the sentence capitalized.


lines = []
while True:
    l = input()
    if l:
        lines.append(l.upper())
    else:
        break;

for l in lines:
    print(l)