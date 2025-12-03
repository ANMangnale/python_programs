n=int(input("Enter Number: "))
fact=1
add=0
x=n
while n:
    a=n%10 # a=4
    for i in range(1,a+1):
       fact=fact*i
    add=add+fact
    fact=1
    n=int(n/10)
print(add)
if add==x:
    print("Strong Number")
else:
    print("Not Strong Number")


    