#Write a Python program that accepts a hyphen-separated sequence of words as 
# input and prints the words in a hyphen-separated sequence after sorting them alphabetically.

print("Enter a hyphen separated sequence of words: ")
items=[n for n in input().split('-')]
items.sort()
print("Sorted: ")
print('-'.join(items))

