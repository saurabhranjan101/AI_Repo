# revenue = 50
# expenses = 10
# print(type(revenue))

# print(f"Profit is {revenue- expenses}")
# s = "I love samosa"
# print(len(s))

# revenue = [50,60,55]
# expenses = [10,30,35]
# margin = []
# # print(type(revenue))
# # print(revenue[-1])
# # print(revenue[1:3]) #n to n-1
# # print(len(revenue))
# for i in range(len(revenue)):
#     profit = revenue[i] - expenses[i]
#     margins = profit * 100/revenue[i]
#     print(f"Margin of Q{i+1} Quarter is - {margins:.2f}")
#     #print(f"Profit of Q{i+1} Quarter is - {profit}")
#     margin.append(round(margins,2))
# print(margin)


##Dictory

# fin = {
#     'revenue': 50,
#     'expense':10
# }

# print(type(fin))
# fin['profit'] = fin['revenue'] - fin['expense']
# print(fin['profit'])


# financials = [
#     {'revenue': 50,'expense':10}, #Q1
#     {'revenue': 60,'expense':30}, #Q2
#     {'revenue': 55,'expense':35}  #Q3
# ]
# j = 1
# for i in financials:
#     profit = i['revenue'] - i['expense']
#     print(f"Profit of Q{j} is {profit}")
#     j +=1

#Nested dictionary
# financials = {
#     "Q1" :{'revenue': 50,'expense':10},
#     "Q2" :{'revenue': 60,'expense':30},
#     "Q3" :{'revenue': 55,'expense':35}
# }
# for quarter, data in financials.items():
#     margin = (data['revenue'] - data['expense'])/data['revenue'] *100
#     print(f'{quarter}:{margin:.2f}%')


# financials = {
#     "Q1" :{'revenue': 50,'expense':10},
#     "Q2" :{'revenue': 60,'expense':30},
#     "Q3" :{'revenue': 55,'expense':35},
#     "Q4" :{'revenue': -10,'expense':35},
# }
# for quarter, data in financials.items():
#     if(data['revenue'] <= 0):
#         print(f"Invalid revenue for {quarter}. skipping")
#         continue
#     margin = (data['revenue'] - data['expense'])/data['revenue'] *100
#     print(f'{quarter}:{margin:.2f}%')

#Tuple
purple = (128,0,128)
yellow = (256,56,0)
mixed = (purple[0] + yellow[0])//2, (purple[1] + yellow[1])//2,(purple[2] + yellow[2])//2
print(mixed)
r,g,b = purple
print(purple[0])
print(purple)
print(r)
print(g)
print(b)