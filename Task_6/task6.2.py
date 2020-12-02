#Write a program to construct a dictionary from the two lists containing the names of students and
#their corresponding subjects. The dictionary should map the students with their respective subjects.
#Let’s see how to do this using for loops and dictionary comprehension.

student = ['Smit', 'Jaya', 'Rayyan']
capital = ['CSE', 'Networking', 'Operating System']

dict = {student: capital for (student,capital) in zip(student,capital)}
print(dict)