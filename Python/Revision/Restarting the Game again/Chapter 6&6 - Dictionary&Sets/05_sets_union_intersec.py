s1 = {1,45,6,78}
s2 = {1,54,5,78}
print(s1.union(s2)) #merge both and keep only unique
print(s1.intersection(s2)) #keep only common from both the sets
print({1,6}.issubset(s1))