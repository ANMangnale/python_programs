# Given a number n, find the first digit of the number.

n=765
while n:
    a=n%10
    n=int(n/10)
print(a)
