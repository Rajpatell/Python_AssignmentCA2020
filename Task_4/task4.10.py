#Write a program which uses filter() to make a list whose elements are even numbers between 1
#and 20 (both included)

lis1 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20] 
  
is_even = lambda x: x % 2 == 0
lis2 = list(filter(is_even, lis1))  
print(lis2) 