x = [10,20,30]
x.append(23)
print(len(x))



cars = ["Porsche","BMW","Audi"]
trending = []
for c in cars:
    if c == "BMW" or "Porsche":
        trending.append(c)
print(trending)


list = [3,1,2,2,2,3]
list.remove(3) #this will remove 3 then we will have this - [1,2,2,2,3]
list.pop(3) #[1,2,2,3]
print(list)