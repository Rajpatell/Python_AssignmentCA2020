
#task 1
def foo():
    try:
        return 1
    finally:
        return 2
k = foo()
print(k)

#it will return 2


#task 2

def a():
    try:
        return 1
    finally:
        print('after f')
        print('after f?')
a()

#output will be:
#after f
#after f?