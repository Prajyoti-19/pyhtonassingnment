# 1. Write a Python program to combine two dictionary adding values for common keys. 
d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
d3={}

for k1,v1 in d1.items():
    for k2,v2 in d2.items():
        if k1==k2:
            c=v1+v2
            d3[k1]=c
            
for k1,v1 in d1.items():
    if k1 not in d3:
        d3[k1]=v1

for k2,v2 in d2.items():
    if k2 not in d3:
        d3[k2]=v2

print(d3)

# 2. Write a Python program to print all unique values in a dictionary. Original List: [{'V': 'S001'}, {'V': 'S002'}, {'VI': 'S001'}, {'VI': 'S005'}, {'VII':'S005'}, {'V': 'S009'}, {'VIII': 'S007'}]
d1 =  [{'V': 'S001'}, {'V': 'S002'}, {'VI': 'S001'}, {'VI': 'S005'}, {'VII':'S005'}, {'V': 'S009'},{'VIII': 'S007'}]
s1=set()
for i in d1:
    for value in i.values():
        s1.add(value)

print(s1)


# 3. Write a Python program to create a dictionary from a string. Track the count of the letters from the string.
ss='w3resource'
d1={}
for i in ss:
    count=0
    for j in ss:
        if i==j:
            count+=1
    d1[i]=count
print(d1)


# 4. Get the key corresponding to the minimum value from the following dictionary
sampleDict = { 'Physics': 82, 'Math': 65, 'history': 75}
l1=[]
for value in sampleDict.values():
    l1.append(value)
a=min(l1)

for j,v in sampleDict.items():
    if a==v:
        print(j)


# 5. Combine two dictionary adding values for common keys
dict1 = {'a': 12, 'for': 25, 'c': 9}
dict2 = {'python': 100, 'java': 200, 'for': 300}
dict3={}

for k1,v1 in dict1.items():
    for k2,v2 in dict2.items():
        if k1==k2:
            a=v1+v2
            dict3[k1]=a

for key,val in dict2.items():
    if key not in dict3:
        dict3[key]=val

print(dict3)


# 6. dict1={101:{“Apple” :10, “Mango” :5 }, 102 :{“Apple” :15, “Mango” :8, “Cherry” :5 }, 103: {“Apple” :10} }
# Output: Dict2= {“ Apple” :35, “Mango” :13, “Cherry” :5 }
dict1={101:{'Apple' :10, 'Mango' :5 }, 102 :{'Apple' :15, 'Mango' :8, 'Cherry' :5 }, 103: {'Apple' :10}}
dict2=dict()
for key,val in dict1.items():
    for key2,val2 in val.items():
        dict2[key2]=val2+dict2.get(key2,0)
        
print('dict = ' , dict2)


            








