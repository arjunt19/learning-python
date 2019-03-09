print("dog1111")
# comment
# indents are used instead of curly braces ***indentation matters
thisNumber = 7
print(thisNumber)
thisNumber = float(thisNumber)  # casting
one, two = 1, 2
if isinstance(thisNumber, float):
    print("this checks the variable type")
if isinstance(thisNumber, float) and thisNumber == 7:
    print('checks two things', thisNumber)
myList = []  # array
myList.append(1)
print(myList[0])
# can multiply strings and lists to create repeating sequences
print("hello, %s mr.number" % thisNumber)
print("hello" + " dog")
string = "doggy"
print(len(string))  # length of a string
print('hello')
#python is case sensitive
dog = "dog"
print(dog[1])  # gives u the character at a certain location
print(dog[0:2])  # prints out a range of characters not including 2
dog = input("This is what will be said before asking for input")  # input function
''' 
objects and methods work like in java, using dot notation to call on an objects method
ex: car.drive()

'''
stringNuber = "12"
number = int(stringNuber)
stringAgain = str(number)
print("the {} fat ones {}".format("fat" , "out"))
# replaces curly braces with the substitutes indicated in the format block
yuhrd = "a specific word inside a string can be found using the find method"
print(yuhrd.find("word")) # returns index of where it is or -1 if not found
print(yuhrd.replace("specific", "butt"))
colors = ["red", "blue", "purple"]  # 0 based and mutable
colors.index("blue")
# tuples are immutable lists
# dictonaries use key value pairs, values can be anything while keys have to immutable
myFile = open("hello.txt", "r")
stringy = myFile.readline()
print (stringy)
myFile.close()
