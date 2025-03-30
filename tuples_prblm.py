# 1. Write a Python program to create a tuple.
l1=[35,64,27,97,13,42,67]
t1=tuple(l1)
print(t1)
          # OR
def tuplecreate(a,b):
    return a+b,a-b,a*b,a+b-4,a+2,b-3

res=tuplecreate(4, 7)
print(res)


# 2. Write a Python program to create a tuple with different data types
l1=[1,4,2,6,'d',3,['to','the','in'], 8.5, 'phone']
t1=tuple(l1)
print(t1)
          # OR
def tuplecreatediff(a,b,c,d):
    return a+b,a-b,d,a*b,a/b,c,

res=tuplecreatediff(4, 7, 'hello','q')
print(res)


# 3. Write a Python program to create a tuple with numbers and print one item
t1=(35,64,27,97,13,42,67)
print(t1[3])
            # OR
def tuplenum(a,b):
    return a+b,a-b,a*b,a+b-4,a+2,b-3

res=tuplenum(4, 7)
print(res)
a=int(len(res)/2)
print(res[a])


# 4. Write a Python program to unpack a tuple in several variables.
t1=(43,56,75,['to','the','in'],4.5)
a,b,c,d,e = t1
print(a)
print(b)
print(c)
print(d)
print(e)

# 5. Write a Python program to add an item in a tuple.
t1=(35,64,27,97,13,42,67)
l1=list(t1)
l1.append(23)
print(l1)

# 6. Write a Python program to convert a tuple to a string.
t1=('we','all','are','one')
a=""
for i in t1:
    a=a+i
print(a)


# 7. Write a Python program to get the 4th element and 4th element from last of a tuple.
t1=(35,64,27,97,13,42,67,37,54)
a=len(t1)
print(f'First 4th element is {t1[3]}')
b=a-3
print(f'Last 4th element is {t1[b]}')
        

# 8. Write a Python program to reverse a tuple.
t1=(35,64,27,97,13,42,67,37,54)
l1=[]
for i in range(len(t1)-1, -1, -1):
    print(t1[i])
    l1.append(t1[i])
t2=tuple(l1)
print(t2)


# 9. Write a Python program to find the repeated items of a tuple
t1=(35,64,27,97,13,64,67,37,97,13)
l1=[]
for i in t1:
    count=0
    for j in t1:
        if i==j:
            count+=1
            if count>=2:
                l1.append(i)

s1=set(l1)
t2=tuple(s1)
print(f'These are the Repeated Elements: {t2}')
            

# 10. Write a Python program to check whether an element exists within a tuple.
t1=(35,64,27,97,13,64,67,37,97,13)
if len(t1)<=0:
    print('Element not exists in tuple')
else:
    print('Element exists in tuple')


# 11. Write a Python program to convert a list to a tuple.
l1=[35,64,27,97,13,42,67]
t1=tuple(l1)
print(t1)


# 12. Write a Python program to remove an item from a tuple.
t1=(35,64,27,97,13,42,67,37,54)
l1=list(t1)
l1.remove(97)
t2=tuple(l1)
print(t2)
            # OR
t1=(35,64,27,97,13,42,67,37,54)
a=int(len(t1)/2)
l1=list(t1)
l1.remove(l1[a])
t2=tuple(l1)
print(t2)

# 13. Write a Python program to slice a tuple.
t1=(35,64,27,97,13,42,67,37,54)
for i in range(3,len(t1),2):
    print(t1[i])


# 14. Write a Python program to find the index of an item of a tuple.
t1=(35,64,27,97,13,42,67,37,54)
for i in range(len(t1)):
    print(f'Element {t1[i]} is in {i} index')


# 15. Write a Python program to find the length of a tuple.
t1=(35,64,27,97,13,42,67,37,54)
print(f'The length of a tuple is {len(t1)}')
        # OR
count=0
for i in range(len(t1)):
    count+=1
print(f'The length of a tuple is {count}')


# 16. Write a Python program to sort list of tuple based on sum
l1= [(4, 5), (2, 3), (6, 7), (2, 8)]
l2=[]
l3=[]
for i in l1:
    l2.append(sum(i))
    a=sorted(l2)
    
for j in a:
    for i in l1:
        if j==sum(i):
            l3.append(i)
print(l3)


