'''
#Greeting message with user name

def fun():
    first_name="Anjali"
    last_name="Mangnale"
    print("Welcome" ,first_name , last_name , )  
fun()

# Adds two numbers by taking user input

def sum():
    n1 = int(input("Enter 1st number : "))
    n2 = int(input("Enter 2nd number : "))
    return n1+n2
    
print(sum())

#Calculator

def fun(num1,op , num2):
    if op=="+":
        return num1+num2
    elif op=="-":
        return num1-num2
    elif op=="*":
        return num1*num2
    else:
        return num1/num2

num1= int(input("Enter Number : "))
op = input("Enter sign : ")
num2 = int(input("Enter Number : "))
 
x=fun(num1 , op , num2)
print(x)

# Square of Arguments

def square(n):
    x= n**2
    print(x)

n=int(input("Enter the Number : "))
square(n)

#factorial of a Number                      

def fact(n):
    f=1
    for i in range(1,n+1):
        f=i*f  
    print(f)       
n=int(input("Enter input : "))
fact(n)

# Print Numbers Between Start to end
def count(start , end):
    for i in range(start, end+1):
        print(i)
        
start = int(input("Enter starting Number : "))   
end = int(input("Enter ending Number : "))   
count(start , end)

# Calculate area of triangle
# 1) Pass Arguments as a Variables
def area(w,h):
    A = w*h
    return A    
w = 5
h= 6
print(area(w,h))

#  2) Pass Arguments as a values
def area(w,h):
    A = w*h
    return A  
print(area(5,6))


# Computes power of Number
def power(n,p):
    x=n**p
    return x    
n = int(input("enter No. : "))
p = int(input("Enter power : "))
print(power(n,p))

# Computes Type of passed Arguments

def fun(n,a):
    return type(n) , type(a)
n=4
a=5.6
print(fun(n,a))
'''

# Age Calculator

def calculateAge(p,q):
    return (q-p) 

a=int(input("Enter Birth Year : "))
b=int(input("Enter current Year : "))
x=(calculateAge(a,b))
print("You are either " f"{x} or {x+1}")

# call the functions for three times with different sets of value
def calculateAge(p,q):
    return (q-p) 
for i in range(3):
    a=int(input("Enter Birth Year : "))
    b=int(input("Enter current Year : "))
    x=(calculateAge(a,b))
    print("You are either " f"{x} or {x+1}")



