# Print 1 To N Without Loop
'''
i=1
def Numbers(n): #Function define
    global i
    if i<=n:
        print(i)
        i=i+1
        Numbers(10)

Numbers(10)'''# Function call

# # Print 1 To N in reverse order without loop
i=1
def Reverse_numbers(n):        
     global i
     if n>=i:
        print(n)
        x=n-1
        Reverse_numbers(x)

Reverse_numbers(10)

