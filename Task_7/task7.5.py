#Write a Person class with an instance variable “age” and a constructor that takes an integer as a
#parameter. The constructor must assign the integer value to the age variable after confirming the
#argument passed is not negative; if a negative argument is passed then the constructor should set
#age to 0 and print “Age is not valid, setting age to 0”. In addition, you must write the following instance
#methods:

#yearPasses() should increase age by the integer value that you are passing inside the function.
#amIOld() should perform the following conditional actions:I
#f age is between 0 and <13, print “You are young”.
#If age is >=13 and <=19 , print “You are a teenager”.
#Otherwise, print “You are old”.

class Person():
    def __init__(self, age):
        if age > 0:
            self.age = age
        else:
            print("Age is not valid ! Age set to 0 again.")
            self.age = 0

    def yearPasses(self):
            print(self.age, "years passed!", self.age + 1, "Running")

    def amIOld(self):
        if self.age <= 12:
            print("You are young")
        elif self.age in range(13, 19):
            print("You are a teenager")
        elif self.age in range(19,61):
            print("You are an adult")
        else:
            print("You are old")

p = Person(int(input("Enter your age : ")))
p.yearPasses()
p.amIOld()
