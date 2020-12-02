#Define a function which can generate and print a tuple where the values are square of numbers
#between 1 and 20 (both 1 and 20 included).

def squarelist(): 
	l=[] 
	for i in range(1,21): 
		l.append(i*i) 
	return l 
 
l=[] 
l=squarelist() 
print(l) 