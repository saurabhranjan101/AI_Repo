d = {}
print(type(d))

marks = {
"Harry":100,
"Shubham":85,
"Rohan":56
}
print(marks.items()) #Item method- this prints all the values
print(marks.keys()) #Print only keys
print(marks.values()) #Print only values
marks.update({"Harry":99,"Renuka":100})
print(marks)
print(marks.get("Shivika")) #returns None
print(marks["Shivika"]) #returns error