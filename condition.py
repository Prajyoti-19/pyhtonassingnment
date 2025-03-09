# age = int(input('Enter Age: '))

# if age>18:
#     print('yoy are above 18 you are allowed')
# else:
#     print('you are not allowed')
    

# # If elif, else condition
# percentage = int(input('Enter Percentage: '))
# if percentage>80:
#     print('A+')
# elif percentage>60 and percentage<80:
#     print('A')
# elif percentage>50 and percentage<60:
#     print('B+')
# elif percentage>40 and percentage<50:
#     print('B')
# else:
#     print('Fail')


# nested loop
a,b,c = 10,20,30

if a<b:
    if b<c:
        if a<c:
            print ('Inside the nested loop')
        else:
            print('else block')
    else:
        print('')
else:
    print('')


# Logical
if a<b and b<c and a<c:
    print('logical')


# Switch Case
print('1. Hindi')
print('2. Marathi')
print('3. English')

option = int(input('Enter input: '))
match option:
    case 10: print('you have selected Hindi')
    case 20: print('you have selected Marathi')
    case 30: print('you have selected English')
    case default: print('you have selected onather one')