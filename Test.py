#A7 2

# t1 = (2,4,3,5,8)
# t2 = ()
# t2 = t1[::-1]
# print (t2)



#A7 3

# t1 = (1,2,3,4,5,6)
# print (t1[0:len(t1)])



#A7 4

# c =0 
# l = [1,2,3,4,5,6,7,('a','b')]
# for i in range (0,len(l)):
#     if type (l[i]) != tuple:
#         c = c+1
#     else:
#         break
# print (c)



#A7 5

# t = (2,3,4,54,5,7)
# print (t.index(3))
# a = "Iman is a good boy"
# print ("The string tuple is:" ,tuple (a))
# b = tuple (a)
# print (b.index('a',2,9))
# z = input ("Enter the element if its present in string tuple or not:")
# try:
#     print (b.index (z,0))
# except:
#     print ("Item not in tuple")



#A7 6

# t1 = (1,2,3,4,5,6,7,7,8)
# print (t1[0:-1])
# print (t1[0:6:2])
# print (t1[0:4])
# print (t1[-3:-1])
# print (t1[0:4])



#A7 7

#LINEAR SEARCH
# t1 = (1,2,3,4,5,6,78,8,9)
# flag = 0
# z = int (input ("Enter the data to be searched: "))
# for i in range (0,len(t1)):
#     if (t1[i] == z):
#         flag = 1
#         break
# if (flag == 0):
#     print ("Item not found ")
# else:
#     print ("Item found")        


def prime(n):
    c= 0
    for i in range (1,n+1):
        if (n%i == 0):
            c = c+1
    if c == 2:
        pass
    else:
        return (n)
s1 = {2,4,6,8}
l = []
i =0
for x in range (1,21):
    a = prime(x)
    l.append(a)
s2 =set(l)
print (s2)