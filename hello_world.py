print("Hello Sunil")
#add two number
a=45
b=24
sum=a+b
print(sum)
print("sum of two number",sum)
print("sum of %a and %b",a,b,sum)

#find the square Root
num=8
num_sqrt=num*2
print('The square root of',num_sqrt)
print('The square root of %0.3f is %0.3f'%(num ,num_sqrt))

#python program to find the area of triangle
a=5
b=6
c=7
s=(a+b+c)/2
area=(s*(s-a)*(s-b)*(s-c))**0.5
print('the area of the triangle is %0.2f'%area)

#5. quadratic equation
import cmath
a=1
b=5
c=6
d=(b**2)-(4*a*c)

sol1=(-b-cmath.sqrt(d))/(2*a)
sol2=(-b+cmath.sqrt(d))/(2*a)
print('The Solution are {0} and {1}'.format(sol1,sol2))

#.6 Swap to variable
 
a=5
b=6
print('value of a={0} and b={1} before swap'.format(a,b))
temp=a
a=b
b=temp
print('value of a={0} and b={1} after swap'.format(a,b))

#.6 Swap to variable

a=5
b=6
print('value of a={0} and b={1} before swap'.format(a,b))
a=a+b
b=a-b
a=a-b
print('value of a={0} and b={1} before swap'.format(a,b))

#generate a random number between 0 and 20

import random

print('random number=',random.randint(0,20))

#10 number or +ve or not

num=int(input("Enter a number:"))
if num>0:
    print("Postive number")
elif num==0:
    print("zero")
else:
    print("Negative nymber")

#12 Check if year is a leap or not

year=2000
if(year%400==0) and (year%100==0):
    print("{0} is a leap year".format(year))
elif(year%4==0) and (year%100!=0):
    print("{0} is a leap year".format(year))
else:
    print("{0} is not a leap year".format(year))