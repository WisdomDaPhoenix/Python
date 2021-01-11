#The isinstance() function returns True if the specified object is of the specified type, otherwise False.

#If the type parameter is a tuple, this function will return True if the object is one of the types in the tuple.

#Syntax: isinstance(object, type) e.g isinstance(x, int) or isinstance(x, str). That is if m is an integer...
#Examples:
# x = isinstance(5, int) Check if the number 5 is an integer and x returns True when printed
# x = isinstance("Hello", (float, int, str, list, dict, tuple)) x returns True because "Hello" is a string and str (string) is in the list of specified types
#Returns all integers in k as a list called t
k = [1,2,'aasf','1','123',123]
t = []
i = 0
while i < len(k) and k[i] in k:
    x = isinstance(k[i], int)
    if x:
        t.append(k[i])
    i = i + 1
print(t)
print()


#Returns all integers in k only
K = [1,2,'aasf','1','123',123]
t = []
for item in K:
    x = isinstance(item, int)
    if x:
        t.append(item)
print(t)



    
#Returns all integers in p as a list called t
p = [1,'a','b',0,15]
t = [m for m in p if isinstance(m, int)]
print(t)




