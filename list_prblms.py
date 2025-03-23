# Create list of cities & display it using for in loop
l1=['africa','boisar','sangli','pune']
for i in l1:
    print(i)

# Modify the city from index 1
l1[1]='satara'
print(l1)

# Display list using print()
print(list(l1))


# 1. WAP to remove to find duplicates elements in list,
l1=[77,56,48,77,23,77,48,77,12,23]
for i in l1:
    count=0
    for j in l1:
        if i==j:
            count=count+1
            if count>=2:
                l1.remove(j)
print(l1)

           
# 2. WAP to sort the given list
l1=[45,77,23,45,66,88,22,12]
print(l1.sort(reverse=True))


# 3. WAP to create a list such that new list contains alternate even and odd from given list
l1=[45,77,23,45,66,88,22,12]
l2=[]
l3=[]
l4=[]
for i in l1:
    if i %2 !=0:
        l2.append(i)
    else:
        l3.append(i)
    
for i in range(len(l2)):
    l4.append(l2[i])
    l4.append(l3[i])
print(l4)

# 4. Write a Python program to get the largest number from a list.
print('max element ',max(l1))


# 5. Write a Python program to count the number of strings where the string length is 2
l1=['in','out','book','to','page','go','pen','is']
count=0
for i in l1:
    if len(i)<=2:
        count+=1;
print(f'Less than string length 2 count is {count}')
        

# 7. Write a Python program to find the list of words that are longer than given words
l1=['red', 'chair', 'book', 'blackboard', 'charger']
l2=[]
n=input('Enter any word: ')
for i in l1:
    if len(n) < len(i):
        l2.append(i)
print(l2)


# 8. Write a Python function that takes two lists and returns True if they have at least one common member.
def find_common(a,b):
    for i in a:
        for j in b:
            if i == j:
                return "true"

l1=['red', 'chair', 'book', 'blackboard', 'charger']
l2=['pizza', 'charger', 'vaseline', 'mobile']
res=find_common(l1,l2)
print(res)


# 9. Write a Python program to print a specified list after removing the 0th, 4th and 5th
sl=['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
sl.pop(5)
sl.pop(4)
sl.pop(0)
print(sl)


# Create a list of elements & find the freq of each element in the list
l1=[77,56,48,77,23,77,48,77,12,23]
l2=[]
for i in l1:
    count=0
    for j in l1:
        if i==j:
            count=count+1
    if i not in l2:
        l2.append(i) 
        print(f"{i} is {count} times")


# ============================================List Comprehension=========================================

# WAP to print square of 1-20 numbers using comprehension
result=[i*i for i in range(20)]
print(result)


# WAP to print values if value is <100
l1=[22,301,55,66,200,250,67,92,150]
result=[i for i in l1 if i<=100]
print(result)
