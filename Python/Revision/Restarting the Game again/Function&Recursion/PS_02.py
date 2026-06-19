#Formula: F = (C × 9/5) + 32

def CeltoFare(C):
    return (C * 9/5) + 32
cel = int(input("Enter value in celcius - "))
print(f"Farenheit value of {cel} is {CeltoFare(cel)}")