# try:
#     a = int(input("Enter a number - "))
#     print(a)
# except Exception as e:
#     print(e)
# print("Thank you")


# try:
#     b = int(input("Enter a number - "))
#     print(b)
# except Exception as e:
#     print(e)

# try:
#     b = int(input("Enter a number - "))
#     print(b)
# except ValueError:
#     print("Invalid input, please enter a number")
# except Exception as e:
#     print("Unexpected Error :",e)


try:
    b = int(input("Enter a number - "))
    print(b)
except ValueError:
    print("Not a number!")
else:
    print("No error occured")
finally:
    print("This block always runs")


try:
    c = int(input("Enter a number - "))
    print(c)
except Exception as e:
    print("Unexpected outpur",e)
except ValueError:
    print("Not a number!")
else:
    print("No error occured")
finally:
    print("This block always runs")