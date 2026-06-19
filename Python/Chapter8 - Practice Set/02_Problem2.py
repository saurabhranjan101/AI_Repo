#Write a python program using function to convert Celsius to Fahrenheit.
#c = 5*(f-32)/9

def f_to_c(f):
    
    c = 5*(f-32)/9
    return c
#f = int(input("Enter temperature in Farenhiet - "))
f = int(input("Enter temperature in Farenhiet - "))
c = f_to_c(f)
print(f"{round(c,2)} Degree Celcius")