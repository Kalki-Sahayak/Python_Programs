## QUESTION 1

# x = int(input("Enter 1 to START and -1 to EXIT"))
# while (x!= -1):
#     a = int(input("1st no.= "))
#     b = int(input("2nd no.= "))
#     if type(a)!= int or type (b)!= int:
#         raise TypeError ("PLEASE ENTER INTEGERS ^_^")
#     elif b ==0:
#         raise ZeroDivisionError ("INFINITY WILL BE THE RESULT [NOT ACCEPTED]")
#     else:
#         print (a/b)

## QUESTION 2

# f1 = open("First.txt", "w")
# f1.write("This is a new file\n")
# f1.write("Welcome to my coding world ^_^\n")
# f1.write("Stay Safe\n")
# f1.close()

# f1 = open("First.txt", "r")
# print(f1.read())
# f1.close()

# f1 = open("First.txt", "r")
# data = f1.read()
# for i in range (0,5):
#     print (data[i])
# f1.close()

# f1 = open("First.txt", "r")
# data2 = f1.readlines()
# for j in range (0,2):
#     print (data2[j])


## QUESTION 3

# f1 = open("First.txt", "a")
# f1.write("\nThis is the new line")
# f1.close()
# f1 = open("First.txt", "r")
# print (f1.read())


## QUESTION 4

# f1 = open ("First.txt", "w")
# f1.write ("This line is overwrited")
# f1.close()
# f1 = open ("First.txt", "r")
# print(f1.read())

## QUESTION 5

# b = input ("Enter the file name along with .txt")
# try:
#     f1 = open (b, "r")
#     print(f1.read())
#     f1.close()
# except IOError:
#     print ("The file do not exist")


## QUESTION 6

# c=0
# wrd = 0
# wd = []
# f = open ("First.txt", "w")
# f.write("This is a new file\nThis is Iman here\n Thank you")
# f.close()
# f = open ("First.txt", "r")
# for i in f:
#     c +=1
#     word = i.split()
#     wrd += len(word)
#     wd = []
# print ("No of lines", c)
# print ("No. of words", wrd)

