#Write a function called showNumbers that takes a parameter called limit.
#It should print all the
#numbers between 0 and limit with a label to identify the even and odd numbers.

def showNumbers(limit):
    for x in range(limit + 1):
        if x % 2:
            print(str(x) + ' ODD')
        else:
            print(str(x) + ' EVEN')

showNumbers(3)