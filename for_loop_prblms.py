# For Loop Condition
for data in range(6):
    print(data)

# the 1 to 10 will print and 11 will skip and stop in previous
for a in range(1, 11):
    print(a)

# Start,stop,step
# In positive step whatever no is given that much go go forward  - Increement
for a in range(1, 11, 2):
    print(a)

# In negative step whatever no is given that much go go backward  - Decreement
for a in range(11, 1, -2):
    print(a)


# Problems
# Even no from 121 to 229 using for loop
for a in range(121,229):
    if a%2==0:
        print(a)
        
# Even no from 521 to 229 using for loop
for a in range(229,121,-1):
    if a%2==0:
        print(a)

# All alphabet from using for loop a to z
for a in range(97,123):
    print(chr(a))

# sum of even no between 1 to n
sum=0
n = int(input('Enter number: '))
for a in range(n):
    if a%2==0:
        sum=sum+a
print(sum)

# sum of odd no between 1 to n
sum=0
n = int(input('Enter number: '))
for a in range(n):
    if a%2==0:
        continue
    sum=sum+a
print(sum)

# star program
row = 1
while row<=5:
    col=1
    while col<=5:
        print('* ',end="")
        col+=1
    print()
    row+=1

# star program
row = 1
col=1
while row<=5:
    j=1
    while j<=col:
        print('* ',end="")
        j+=1
    print()
    row+=1
    col+=1


# 12345 program
row = 1
col=1
while row<=5:
    j=1
    while j<=col:
        print(j,end="")
        j+=1
    print()
    row+=1
    col+=1


# star program in for loop
col=1
for row in range(0,5):
    for j in range(0,col):
        print('* ',end="")
    print()
    col+=1


# 12345 program
col=1
for row in range(1,7):
    for j in range(1,col):
        print(j ,end="")
    print()
    col+=1


# Q1)
# * * * * * 
# * * * * 
# * * * 
# * * 
# * 
# In while Loop
row =1
col=1
while row<=5:
    j=5
    while col<=j:
        print('* ',end="")
        j-=1
    print()
    row+=1
    col+=1



# Q2)
# 1 
# 2 3 
# 4 5 6 
# 7 8 9 10 
# In while Loop
row =1
j=1
i=1
while row<=4:
    col=1
    while col<=j:
        print(i ,end=" ")
        i+=1
        col+=1
    print()
    row+=1
    j+=1

# In For Loop
k=1
for row in range(1,6):
    for j in range(1, row):
        print(k, end=" ")
        k+=1
    print()



# Q3)
# 1 
# 2 1 
# 3 2 1 
# 4 3 2 1 
# 5 4 3 2 1 
# In while Loop
row = 1
j=1
p=1
while row<=5:
    col=1
    p=row
    while col<=j:
        print(p ,end=" ",)
        col+=1
        p-=1
    print()
    row+=1
    j+=1
    p+=1

# In For Loop
k=1
for row in range(1,6):
    p=k
    for j in range(0, row):
        print(p, end=" ")
        p-=1
    print()
    k+=1


# 1 2 3 4 5 
# 2 3 4 5 
# 3 4 5 
# 4 5 
# 5 
# In while Loop
row =1
col=5
j=1
while row<=5:
    k=row
    col=5
    while row<=col:
        print(k, end=" ")
        k+=1
        col-=1
    print()
    row+=1

# In For Loop
k=1
for row in range(1,6):
    k=row
    for j in range(row,6):
        print(k, end=" ")
        k+=1
    print()


# 1 
# 1 2 1 
# 1 2 3 2 1 
# 1 2 3 4 3 2 1 
import math
row=1
k=1
while row<=4:
    col=1                    # row = 3, k=5, col= 4
    b=(math.ceil(k/2))
    while col<=k:
        if col>=(math.ceil(k/2))+1:
            b-=1
            print(b, end=" ")
        else:
            print(col, end=" ")
        # half=math.ceil(col/2)
        col+=1
    print()
    row+=1
    k+=2
    

