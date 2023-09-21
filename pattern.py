def left_right_tri():
    n = int(input("Enter the number of rows: "))
    for i in range (1,n+1):
        for j in range (1,i+1):
            print ('*', end = "")
        print ()
def right_right_tri():
    n = int(input("Enter the number of rows: "))
    for i in range (1,n+1):
        for k in range (1,n+1-i):
            print (" ", end ="")
        for j in range (1,i+1):
            print("*",end="")
        print ()
def tri():
    n = int(input("Enter the number of rows: "))
    for i in range (1,n+1):
        for k in range (1,n+1-i):
            print (" ", end ="")
        for j in range(1,i+1):
            print (" *",end="")
        print ()
def num_right():
    n =int(input("Enter the number of rows: "))
    for i in range (1,n+1):
        for j in range (1,i+1):
            print ("%d"%j, end="")
        print ()
def num_right_continuous():
    n =int(input("Enter the number of rows: "))
    a=1
    for i in range (1,n+1):
        for j in range (1,i+1):
            print ("%-3d"%a, end="")
            a+=1
        print ()
        