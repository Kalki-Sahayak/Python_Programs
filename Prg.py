# l1 = [1, 2, 3]
# # l2 = [l1, 12, 13]
# # l1.append (4)
# # print (l1)
# # l1.append (('5a', '5b'))
# # print (l1)
# # l1.extend (l2)
# # print (l1)
# # print (l2)





# # l1.insert (5,'six')
# # l1.index ('six')
# # print (l1)
# # l1.pop(4)
# # print (l1)
# # l1.remove ('six')
# # print (l1)
# # print (l1.reverse())
# # l1.remove (('5a','5b'))
# # print (l1.sort())




# print ('p' in l1)
# print ('2'in l1)
# cubes = [x**3 for x in range (10)]
# print (cubes)


#HISTOGRAM (Question 2)

# values = []
# print ("Enter 10 intergers: ")
# for i in range (10):
#         newValue = int(input("Enter integer %d: " %(i+1)))
#         values.append(newValue)
#         print ("%s %10s %10s"%("Element", "Value", "Histogram"))
#         for i in range (len(values)):
#                 print ("%7d %10d %s" % (i,values[i], "*" * values[i]))


#PLAYERS (Question 3)

# playList = []
# print ("Enter the 5 Shakespareean person plays.\n")
# for i in range (5):
#         playName = input("Play %d:" %(i+1))
#         playList.append (playName)
#         print ("\n Subscript Values")
#         for i in range (len(playList)):
#                 print ("%9d %-25s" %(i+1,playList[i]))




# MATRIX (Question 5)

# t1 = [[1,2,3],[4,5,6]]
# print ("The values of the table are: ")
# for row in t1:
#         for item in row:
#                 print (item,end ="")
#         print ()




#FREQUENCY (Question 7)

# x = input ("Enter string: ")
# x = list(x)
# y = list(set(x))
# c = []
# for i in range (len(y)):
#         c.append(x.count (y[i]))
#         print (y[i],c[i])


#COMPARE (Question 6)

# a = []
# b = []
# c =0
# x = int (input ("Enter the elemnets of the lists: "))
# for i in range (x):
#         c = int(input("Enter the elements of 1st list: "))
#         a.append (c)
# for j in range (x):
#         d = int(input("Enter the elements of 2nd list: "))
#         b.append(d)
# for i in range (x):
#         for j in range (x):
#                 if (a[i]==b[j]):
#                         c+= 1
# if (c == x):
#         print ("Same")
# else:
#         print (" Not Same")




#STACK (Question 8)

# a = []
# x = int(input ("\n TO EXIT PRESS -1\n"))
# while (x != -1):
#         print ('1. Push')
#         print ('2. Pop')
#         b = int (input ("Enter your choice: "))
#         if b==1:
#                 print ("Which type of element you want to enter")
#                 print ("1. Words")
#                 print ("2. Numbers")
#                 print ("3. Others")
#                 c = int(input("Enter your choice: "))
#                 if c == 1:
#                         d = input ("Enter the word: ")
#                         a.append(d)
#                         print ("The list is :", a)
#                 if c == 2:
#                         d = int(input ("Enter the number: "))
#                         a.append(d)
#                         print ("The list is: ",a)
#                 if c == 3:
#                         d = input ("Enter the element: ")
#                         a.append(d)
#                         print ("The list is: ",a)
#         if b==2:
#                 if (len(a)== 0):
#                         print ("Empty List")
#                 else:
#                         print ("The popped element is", a.pop())
#                         print ("The list is :", a)


# QUEUE (Question 9)

# a = []
# x = int(input ("\n TO EXIT PRESS -1\n"))
# while (x != -1):
#         print ('1. Insert')
#         print ('2. Delete')
#         b = int (input ("Enter your choice: "))
#         if b==1:
#                 print ("Which type of element you want to enter")
#                 print ("1. Words")
#                 print ("2. Numbers")
#                 print ("3. Others")
#                 c = int(input("Enter your choice: "))
#                 if c == 1:
#                         d = input ("Enter the word: ")
#                         a.append(d)
#                         print ("The list is :", a)
#                 if c == 2:
#                         d = int(input ("Enter the number: "))
#                         a.append(d)
#                         print ("The list is: ",a)
#                 if c == 3:
#                         d = input ("Enter the element: ")
#                         a.append(d)
#                         print ("The list is: ",a)
#         if b==2:
#                 if (len(a)== 0):
#                         print ("Empty List")
#                 else: 
#                         print ("The Deleted element is: ", a.pop(0))
#                         print ("THe list is: ", a)