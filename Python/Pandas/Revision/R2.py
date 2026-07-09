import pandas as pd
data = {
'Name':['Saurabh','Ranjan','A','B'],
'Age' :[35,34,29,19],
'Salary' : [140000,3500000,180000,950000]
}
df = pd.DataFrame(data)
print(df.Name == "Saurabh") #this will retun output in True & False
print(df[(df.Name == "Saurabh")]) #Over true & false - this will return only the true output

#where condition
print(df.where(df.Name == "Saurabh"))
# print(df.where(df['Age'] > 30))