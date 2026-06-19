#Write a python function to remove a given word from a list and strip it at the same time.
'''

'''
def rem(l,word):
    for item in l:
         l.remove(word)
    return
l = ["Saurabh","Rohan","Ram","an"]
print(f"{rem(l,"an")}")