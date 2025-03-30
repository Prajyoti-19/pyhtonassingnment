a = 1
while a<=10:
    print('hello')
    a+=1

# Increement
while a<=10:
    print(a)
    a+=1

# Decreement
a = 10
while a>=1:
    print(a)
    a-=1

# Even Number
a = 100
while a>=1:
    if a%2==0:
        print(a)
    a-=1


# Odd Number
a = 100
while a>=1:
    if a%2 != 0:
        print(a)
    a-=1

# Sum of 20 numbers
a = 1
sum = 0
while a<= 10:
    sum += a
    a += 1
print('Sum is ' , sum)


# Even no from 121 to 229 using while loop
a = 121
print('Even no from 121 to 229')
while a <= 229:
    if a%2==0:
        print(a)
    a+=1


# Even no from 521 to 229 using while loop
a = 521
print('Odd no from 521 to 229')
while a >= 229:
    if a%2 != 0:
        print(a)
    a-=1


# All alphabet from using for loop a to z
a = 97
print('Alphabet using a to z')
while a<=122:
    print(chr(a))
    a+=1


# sum of even no between 1 to n
a = 2
sum = 0
print('sum of even no between 1 to n')
n = int(input('Enter number : '))
while a<=n:
    sum+=a
    a+=2
print('sum of 1 to n even is : ',sum)
    

# sum of odd no between 1 to n
a = 1
sum = 0
print('sum of odd no between 1 to n')
n = int(input('Enter number : '))
while a<=n:
    sum+=a
    a+=2
print('sum of 1 to n odd is : ',sum)


# count no of digits in any number
print('count no of digits')
n = int(input('Enter number : '))
a = 0
count = 0
while a<n:
    count+=1
    n//=10
print(count)


# print table of given no
print('table of given no')
a = 1
mul = 0
b = int(input('Enter number : '))
while a <= 10:
    mul = b * a
    print(mul)
    a+=1


# print squares from 1 to 20
print('squares from 1 to 20')
a = 1
mul = 1
while a <= 20:
    mul = a * a
    print(mul)
    a+=1


# check no is prime or not
print('check no is prime or not')
n = int(input('Enter number : '))
b = n
a = 2
while a <= n:
    n-=1
    if b%n != 0:
        if n == 2:
            print('It is prime no')


# Check no is armstong no
print('Check no is armstong no')
n = int(input('Enter number : '))
b = n
sum = 0
while n!=0:
    r=n%10
    sum=sum+(r*r*r)
    n//=10
    
if b==sum:
    print("Its a Armstrong no")
else:
    print("Its not a Armstrong no")


# WAP to print alternate character from the given string
n=(input("Enter a word: "))
f=""
for i in n:
    c=ord(i)+1
    d=chr(c)
    f=f+d
print(f)
