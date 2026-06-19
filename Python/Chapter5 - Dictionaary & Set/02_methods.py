d = {} #Empty dictionary
marks = {
    "Saurabh" : 100,
    "Pawan" : 50,
    "Sandeep":25,
    "list":[1,2,9],
    0:"Monu"
}
new_marks = marks.copy()
print("New Marks", new_marks)
# print(marks)
print(marks.items())
# print(marks.keys())
# print(marks.values())
# marks.update({"Saurabh":99,"Renuka":86})
# print(marks)
# last_item = marks.popitem()
# print("Removed Item", last_item)
# print(marks)

# # print(marks.get("Saurabh"))
# # print(marks["Saurabh"])

print(marks.get("Saurabh"))  #This will return None
# # print(marks["Saurabh1"]) #This will throw an error