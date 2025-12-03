'''
****
***
**
*
*
**
***
****
'''

for i in range(0,5):
    for j in range(0,5-i):
        print("*",end="")
    print("\n")
for i in range(0,5):
    for j in range(0,i):
        print("*",end="")
    print("\n")
    
    

'''
1 2 3 4
1 2 3
1 2
1
'''
for i in range(1,5):
    for j in range(1,6-i):
        print(j,end=" ")
    print("\n")

'''
A B C D
A B C
A B
A
'''
for i in range(1,5):
    ch=65
    for j in range(1,6-i):
        print(chr(ch),end=" ")
        ch+=1
    print("\n")

'''
A
A B
A B C 
A B C D
'''
for i in range(1,5):
    ch=65
    for j in range(0,i):
        print(chr(ch),end=" ")
        ch+=1
    print("\n")

'''
    A
   A B
  A B C
 A B C D
A B C D E
'''

for i in range(1,6):
    ch=65
    for k in range(1,6-i):
        print("_",end="")
    for j in range(0,i):
        print(chr(ch),end=" ")
        ch+=1
    print("\n")

'''
    A
   A B
  A B C
 A B C D
A B C D E
 A B C D E
  A B C D 
   A B C 
    A B 
     A 
'''
for i in range(1,6):
    ch=65
    for k in range(1,6-i):
        print("_",end="")
    for j in range(0,i):
        print(chr(ch),end=" ")
        ch+=1
    print("\n")

for i in range(1,6):
    ch=65
    for k in range(1,i):
        print("_",end="")
    for j in range(0,6-i):
        print(chr(ch),end=" ")
        ch+=1
    print("\n")