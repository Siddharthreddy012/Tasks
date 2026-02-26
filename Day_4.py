#Arithmetic Operators


print("Arithmetic Operators : ")

num_1=245
num_2=23
print("num_1 : ",num_1)
print("num_2 : ",num_2)
sum=num_1+num_2
print("Sum of num_1 & and num_2 : ",sum)
sub=num_2-num_1
print("Sub of  num_2 & num_1 : ",sub)
mul=num_1*num_2
print("Mul of num_1 & num_2 : ",mul)
mod=num_2%num_1
print("mod of num_2 & num_1 : ",mod)
floor=num_1//num_2
print("Floor of num_1 & num_2 : ",floor)
exp=num_1**num_2
print("exp of num_1 & num_2 : ",exp )


#Assignment Operators


print("\n Assignment Operators : \n")

print("value of num_1 is : ",num_1)
num_1 += 20
print("value of num_1 is : ",num_1)
num_1 -= 20
print("value of num_1 is : ",num_1)
num_1 *= 20 
print("value of num_1 is : ",num_1)
num_1 /= 20 
print("value of num_1 is : ",num_1)
num_1 %= 20
print("value of num_1 is : ",num_1)
num_1 //= 20 
print("value of num_1 is : ",num_1)
num_ = 123
num_1 **= 20 
print("value of num_1 is : ",num_1)


#Comparison Operators


print(" \n Comparison Operators : \n")

person_1 =54
person_2 =80
com= person_1 == person_2
print(com)
com= person_1 != person_2
print(com)
com = person_1>person_2
print(com)
person_3 =5.8
person_4 =6.0
com= person_4<person_3
print(com)
person_5=75
person_6=50
com = person_5 >= person_6
print(com)
person_7 = 18
com=person_7<=18
print(com)


#Logical Operators

print("\n Logical Operators :\n")

cgpa_1=5.9
cgpa_2=5.5
stmt_1=cgpa_1>cgpa_2
stmt_2=cgpa_2>cgpa_1
res=stmt_1 and stmt_2
print(res)
res=stmt_1 or stmt_2
print(res)
res=not stmt_2
print(res)


#Bitwise Operators

print(" \n Bitwise Operators :\n ")

num_1=100
num_2=85
res=num_1 & num_2
print(res)
res=num_2 | num_1
print(res)
res=num_1 ^ num_2
print(res)
res= ~num_1
print(res)
res=num_1 << num_2
print(res)
res=num_1 >> num_2
print(res)

#Membership Operators

print("\n Membership Operators : \n")

num=[1,2,2,4,5,6,6,8,9,9,0]
print( num)
number= 5 in num
print(number)
number= 3 not in num
print(number)

#Identity Operators

print("\n Identity Operators :\n")
idy=1234
idy_1=1234
check= id(idy) is id(idy_1)
print(check)
check= id(idy) is not (idy_1) 
print(check)


#Real Time Examples

print("\n Real Time Examples : \n")

marks= 85
pass_marks= 60

#Comparison Operator
res = (marks >= pass_marks)
print(res)
res= (marks<pass_marks)
print(res)

# Logical operator 
res = (marks > 80 and pass_marks > 85)
print(res)
res = (not res)
print(res)


#Simple Calculator

print("\n Simple Calculator :\n ")

num1 = int(input('Enter the first number: '))
num2 = int(input('Enter the second number: '))
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
division = num1 / num2 
modulo = num1 % num2
exponential = num1 ** num2
print("num1 + num2 = ", addition)
print("num1 - num2 = ", subtraction)
print("num1 * num2 = ", multiplication)
print("num1 / num2 = ", division)
print("num1 % num2 = ", modulo)
print("num1 ** num2 = ", exponential)


# Checking number properties 
#Bitwise operators

print("\n Bitwise operators : \n")
number = 14
odd = number & 1
even = not odd 
print(odd)
print(even)



