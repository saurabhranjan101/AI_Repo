import datetime
sysdate = datetime.date.today()
print(sysdate)
name = input("Enter your name ")
##date = input("Enter Date ")
letter = f'''\n Dear {name}, \n You are selected! \n {sysdate} '''
print(letter)


#OR
letter = '''Dear <|Name|>, 
You are selected! 
<|Date|> '''
print(letter.replace("<|Name|>","Saurabh").replace("<|Date|>","19th March"))