#String Data Type
#Python Strings are arrays of bytes representing Unicode characters. In Python, there is no character data type Python, a character is a string of length one. It is represented by str class.

#Strings in Python can be created using single quotes, double quotes or even triple quotes. We can access individual characters of a String using index.

s = 'Welcoqme to the geeks world'
print(s)
print(type(s))
# access string with index
print(s[1])
print(s[2])
print(s[-4])

#List Data Type
#Lists are just like arrays, declared in other languages which is an ordered collection of data. It is very flexible as the items in a list do not need to be of the same type.
#Lists in Python can be created by just placing the sequence inside the square brackets[].
a = [] #empty list
print(a)
a = [1,2,3]
print(len(a))
print(a)
b = ['hey', 2,5,"anjali"]
print(b)

#Access List Items
a = ["Geeks", "For", "Geeks"]
print("Accessing element from the list")
print(a[1])
print(a[2])

print("Accessing element using negative indexing")
print(a[-1])
print(a[-3])


#Tuple Data Type - Just like a list, a tuple is also an ordered collection of Python objects. The only difference between a tuple and a list is that tuples are immutable. Tuples cannot be modified after it is created.

#Creating a Tuple in Python - In Python Data Types, tuples are created by placing a sequence of values separated by a ‘comma’ with or without the use of parentheses for grouping the data sequence. Tuples can contain any number of elements and of any datatype (like strings, integers, lists, etc.).

#Note:  Tuples can also be created with a single element, but it is a bit tricky. Having one element in the parentheses is not sufficient, there must be a trailing ‘comma’ to make it a tuple.

tup1 = ()
print(tup1)
tup2 = ('Geeks', 'for')
print("Tuple with the use of String: ", tup2)

#Boolean Data Type in Python - Python Data type with one of the two built-in values, True or False. Boolean objects that are equal to True are truthy (true), and those equal to False are falsy (false). However non-Boolean objects can be evaluated in a Boolean context as well and determined to be true or false. It is denoted by the class bool.

print(type(True))
print(type(False))
#print(type(true)) # true is not a valid keyword in Python. Python is case-sensitive

# Set Data Type in Python - In Python Data Types, Set is an unordered collection of data types that is iterable, mutable, and has no duplicate elements. The order of elements in a set is undefined though it may consist of various elements.
#Create a Set in Python - Sets can be created by using the built-in set() function with an iterable object or a sequence by placing the sequence inside curly braces, separated by a ‘comma’. The type of elements in a set need not be the same, various mixed-up data type values can also be passed to the set.

#Example: The code is an example of how to create sets using different types of values, such as strings , lists , and mixed values

s1 = set() #empty set
s1 = set("GeeksForGeeks") #string
print("Set with the use of String: " , s1)

s2 = set(["Geeks" , "For" , "Geeks"]) #list
print("Set with the use of List: " , s2)

#Access Set Items - Set items cannot be accessed by referring to an index, since sets are unordered the items have no index. But we can loop through the set items using a for loop, or ask if a specified value is present in a set, by using the in the keyword.
s1 = set(["Geeks" , "For" , "Geeks"]) 
print("Set with the use of List: " , s1)
# loop through set
for i in s1 :
    print(i , end=" ")
## check if item exist in set  
print("Geeks" in s1)
print("for" in s1)

#Dictionary Data Type - A dictionary in Python is a collection of data values, used to store data values like a map, unlike other Python Data Types that hold only a single value as an element, a Dictionary holds a key: value pair. Key-value is provided in the dictionary to make it more optimized. Each key-value pair in a Dictionary is separated by a colon : , whereas each key is separated by a ‘comma’.

#Create a Dictionary in Python - Values in a dictionary can be of any datatype and can be duplicated, whereas keys can’t be repeated and must be immutable. The dictionary can also be created by the built-in function dict().

#Note  - Dictionary keys are case sensitive, the same name but different cases of Key will be treated distinctly.

d = {}#empty dictionary
d = {1:'Geeks', 2:'For', 3:'Geeks'}
print(d)
d1 = dict({1:'Geeks', 2:'For', 3:'Geeks'})# creating dictionary using dict() constructor
print(d1)

# Accessing Key-value in Dictionary - In order to access the items of a dictionary refer to its key name. Key can be used inside square brackets. Using get() method we can access the dictionary elements.
d2 = {1:"hey", "name":'hello', 3:"hiiii"}
# Accessing a element using key
print(d2["name"])
 # Accessing a element using get
print(d2.get(3))