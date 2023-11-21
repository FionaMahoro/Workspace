# P_Name ="john Smith"
# P_age =20
# P_admit="New"
# print (P_Name ,P_age, P_admit)


# first_number= input('Enter number: ')
# Second_number= input('Enter number: ')
# sum = int(first_number) + int(Second_number) 
# # Python can only concatnate str
# print ("The sum is " + str(sum))

# str= "python"
# print (str.capitalize())

# Boolean
# num1= 30
# num2= 2

# print (bool (num2 < num1))

# If statement
# a1=1
# a2=2
# a3=3

# if a1 == a2:
#     print("Numbers not equal")
#     a3=0

# print (a3)

#Program to calculate discount for below condition
# total_item=1400
# dis=0

# if total_item >= 1200:
#     dis= 10
# total= total_item- total_item*dis/100
# print(total_item*dis/100)
# print(total)

# name="Jake"
# age=70
# status= 'Minor'

# if age <= 17:
#     print('Minor')

# elif age >= 18 and age <= 64:
#     print('Adult')

# else:
#     print ('Senior citizen')

# # while loop
# num =0
# i= 0
# # the 3 mean you can only input 3 numbers
# while i <3:
#     num= int (input('Number='))
#     if num==0:
#         print('Square is zero')
#         continue
#     if num ==1:
#       print ('Program breaks')
#       break

#     sq= str(num*num)
#     print('Square:' +sq)
#     i +=1
# else:
#     print('Done')

# For in a program

# for e in 'Element':
#     print (e.capitalize())

# lst=[2,10,30,23,4]
# for num in lst:
#     print(num*2)

lst= ['Python','C','Java',12,'Javascript']

for ele in lst:
    
    if ele =='Javascript':
        print(ele)
        continue
    if ele ==12:
        # print("we have invalid item in the list")
        break
    print(ele.upper())
