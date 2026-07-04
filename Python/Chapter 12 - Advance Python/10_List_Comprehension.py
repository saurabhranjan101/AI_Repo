# mylist = [1,2,5,6,9]
# squaredlist = []
# for item in mylist:
#     squaredlist.append(item*item)
# print(squaredlist)

#using list comprehension
mylist = [1,2,5,6,9]
squaredlist = [i*i for i in mylist]
print(squaredlist)