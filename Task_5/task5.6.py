#Read doc.txt file using Python File handling concept and return only the even length string from
#the file. Consider the content of doc.txt as given below:
#Hello I am a file
#Where you need to return the data string
#Which is of even length
#Make sure you return the content in The same link as it is present.


list = []
my_file = open('doc.txt', 'r')
my_str = my_file.readlines()

for i in my_str:
    string = ""
    i = i.strip('\n')
    list = i.split(" ")
    for j in list:
        if len(j) % 2 == 0 :
            string  = string + " " + j
    print(string)

my_file.close()