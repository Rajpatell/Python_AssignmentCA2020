#Flatten the list [1,2,3,4,5,6,7] into 1234567 using reduce().

from functools import reduce
reduce(lambda a,d: 10*a+d, [1,2,3,4,5,6,7], 0)