# 1. Write a program to create a function that takes two arguments, name and age, and print their value.
def nameage(a, b):
    print(f'my name is {a} and age is {b}.')

name = input('Enter name: ')
age= input('Enter Age: ')
nameage(name, age)


# 2. Write a program to create function calculation() such that it can accept two variables and calculate addition and subtraction. Also, it must return both addition and subtraction in a single return call
def calculation(a,b):
    add = a+b
    sub = a-b 
    return add,sub

addition = int(input('Enter 1st no: '))
subtraction = int(input('Enter 2nd no: '))
ad, sb = calculation(addition, subtraction)
print(f'Addition is {ad}, subtraction is {sb}')


# 3. Write a program to create a function show_employee() using the following conditions.
# It should accept the employee’s name and salary and display both.
def show_employee(a,b):
    print(f'my name is {a} and salary is {b}.')

name = input('Enter name: ')
sal= int(input('Enter Salary: '))
show_employee(name, sal)


# 4. Accept a number from the user, create a function isPrime(), which accepts a number from a parameter & check prime or not. If number is prime return True & number else return false & number
def isPrime(no):
    for i in range(2, no):
        if no % i == 0:
            print(f'{no} is not prime no')
            break
        else:
            print(f'{no} is prime no')
            break

nm = int(input('Enter any no: '))
isPrime(nm)


# 5. Create menu driven calculation (add,sub,multiply, divide, mod) using function
def add(a,b):
    return a+b
def sub(a,b):
    return a-b 
def mul(a,b):
    return a*b 
def div(a,b):
    return a/b
def mod(a,b):
    return a%b

no1 = int(input('Enter 1st no: '))
no2 = int(input('Enter 2nd no: '))
print('1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n5. Mod')
no = int(input('Choose an option: '))
if no == 1:
    result = add(no1, no2)
    print(f'Addition is {result}')
elif no == 2:
    result = sub(no1, no2)
    print(f'Subtraction is {result}')
elif no == 3:
    result =  mul(no1, no2)
    print(f'Multiplication is {result}')
elif no == 4:
    result = div(no1, no2)
    print(f'Division is {result}')
elif no == 5:
    result = mod(no1, no2)
    print(f'Mod is {result}')
else:
    print("You didn't choose 1-5")


# 6. Create a function to accept a number & return its factorial
def factorial(n):
    a=1
    for i in range(n, 1, -1):
        a=a*i
    return a

num = int(input('Enter a number: '))
result = factorial(num)
print(f'factorial of {num} is {result}')
        

# 7. Create a function that accept student data, calculate the total & percentage, return total & percentage
def student_marks(a,b):
    outof = a*100
    per = (b/outof)*100
    return b,per

sub = int(input('Enter the subject count: '))
a=0
for i in range(sub):
    mark = int(input('Enter the marks {i}. Subject: '))
    a=a+mark
total, percentage = student_marks(sub, a)
print(f"Your total marks is {total}, and percentage is {percentage}")


# 8. Create a login function, that accept username & password, if username is ‘admin’ & password is ‘admin@123’ then return true, else return false
def login(a,b):
    if (a == 'admin' and b=='admin@123'):
        return "true"
    else:
        return "false"

user = input('Enter Username: ')
passw = input('Enter Password: ')
res=login(user, passw)
print(res)


# 10. Create a function which accept a string & character, check the occurrence of given character in a string and return the count
def count_str(a):
    count=0
    for i in a:
        count+=1
    return count

n = input('Enter any word: ')
result = count_str(n)
print(result)


