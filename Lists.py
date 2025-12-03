# **sum all the items in a list.

a=[ 5,10,15,20]
a=a[0]+a[1]+a[2]+a[3]
print(a)

# o/p : 50

# using for loop
a=[5,10,15,20]
sum=0
for i in a:
    sum=sum+i
print(sum)

# o/p : 50

# using function
def sum_List(n):
    sum=0
    for i in n:
        sum=sum+i
    return sum
print(sum_List([5,10,15,20]))

# o/p : 50

# **multiply all the items in a list.

a=[3,1,2,3]
a=a[0]*a[1]*a[2]*a[3]
print(a)

# o/p : 18

#using for loop
a=[3,1,2,3]
mul=1
for i in a:
    mul=mul*i
print(mul)

# o/p : 18
    
# using function
def mul_List(n):
    mul=1
    for i in n:
        mul=mul*i
    return mul
print(mul_List([3,1,2,3]))

# o/p : 18

# **largest number from a list.

#using built in 
print(max([1,25,78,45]))  

# o/p:78

#using for loop :
a=[1,25,7,4]
max=a[0]
for i in a:
    if i>max:
        max=i
print(max)

# o/p : 25  

#using function :
def max_List(a):
    max=a[0]
    for i in a:
        if i>max:
            max=i
    return max
print(max_List([1,25,78,45]))

# o/p : 78


# **Smallest number from a list.

#using python built-in
print(min([1,25,78,45]))

# o/p:1

# Using for loop
a=[8,-3,22,12]
min=a[0]
for i in a:
    if min>i:
        min=i
print(min)

# o/p : -3

# using function
def min_list(a):
    min=a[0]
    for i in a:
        if min>i:
            min=i
    return min    
print(min_list([8,4,0,2]))

# o/p:0


# **The string length is 2 or more and the first and last characters are the same.

#Using for loop:
list = ['abc', 'xyz', 'aba', '1221']
count=0
for i in list:
    if len(i)>1 and i[0]==i[-1]:
        count+=1
print(count)

# o/p: 2

#using function:
def match_word(list):
    count=0
    for i in list:
        if len(i)>1 and i[0]==i[-1]:
            count+=1
    return count
print(match_word(['sos', 'bye', 'tit','tat']))

# o/p: 3

#**print a specified list after removing the 0th, 4th and 5th elements.

list = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
list.pop(5)
list.pop(4)
list.pop(0)
#del list[0]
#del list[3:5]
#del list[4]
print(list)

 # o /p: ['Green', 'White', 'Black']

 # **clone or copy a list.

a=[28,4,3,'a','g']
b=a.copy()
print(b)

# o/p : [28,4,3,'a','g']

list=[8,45,3,'Des','g']
new_list=list.copy()
print("Original_list :", list)
print("new_list: ", new_list)

# o/p : Original_list : [8, 45, 3, 'Des', 'g']
#      new_list:  [8, 45, 3, 'Des', 'g']