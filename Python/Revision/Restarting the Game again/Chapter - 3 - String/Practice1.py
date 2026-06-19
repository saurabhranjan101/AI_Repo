a = "Saurabh"
print(a[0:3]) #This will print 0,1,2 values. It's always n-1
print(a[1:3])

#Slicing with skip value
word = "amazing"
print(word[1:6:2]) #mzn
print(word[:6])

#String function
b = "Saurabh"
#len() function - this gives the length of a string
print(len(a))
#endswith() - returns true or false
print(b.endswith("bh"))
#startswith() - returns true or false
print(b.startswith("Sa"))