hindi = {
    "Aam":"Mango",
    "Santra":"Orange",
    "dost":"friend"
}
user = input("Enter a hindi word - ")
print(f"English word of the {user} is",hindi.get(user)) #get is a method used to fetch the value you pass to it.