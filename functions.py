
# Function Without arguments
def helloFunction() :
    print("Hello")
    
helloFunction()

# Function With Arguments
def argumentFunction(  a=2,b=3) :
    return a+b
   
    
result=argumentFunction()
print(result)

# Print GFG n times without the loop.
count = 0
def functionGfg():
    n = 5
    global count
    if count < n:
        print("Gfg")
        count = count + 1
        functionGfg()

functionGfg()
