employee={
      "Amol":45000,
      "Rohan":32000,
      "Suraj":42000,
      "Akshay":34000
    }

# Using Lambda 
#       which form result               argument : (expressions          conditions )                , 
#        u want i.e. dict                 we write in function return   
new_emp = dict(map(lambda item: (item[0],item[1]*1.5 if item[1]>40000 else item[1]), employee.items()))
print(new_emp)


# Using functions
d2={}
def test(d1):
    a=0
    for k,v in d1.items():
        if v>40000:
            a=v*1.5
            d2[k]=a
        else:
            d2[k]=v
            
test(employee)
print(d2)

new_emp = dict(filter(lambda item: item[1]>40000, employee.items()))
print(new_emp)



# 2nd Question of Product
product={
      "suitcase":500,
      "bag":2000,
      "book":1500,
      "soap":800
    }

new_prod = dict(map(lambda prod: (prod[0], prod[1]*0.05+prod[1] if prod[1]>1000 else prod[1]), product.items()))
print(new_prod)

new_prod=dict(filter(lambda prod : prod[1]>1000, product.items()))
print(new_prod)