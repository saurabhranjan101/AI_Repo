import pandas as pd
data = {
'Name':['Saurabh','Ranjan','A','B'],
'Age' :[35,34,29,19],
'Salary' : [140000,3500000,180000,950000]
}
df = pd.DataFrame(data)
# print(df)

# #Let's filter for age > 18
print(df[df['Age'] > 30])

print(df[(df["Name"] == "Saurabh") & (df["Age"] > 20)])
print("*******************")
print("*******************")
# #Where method - will retrun the rows where condition is satisfied and also return all the rows with NULL value
print(df.where(df["Age"] > 20, other= "Not Application")) # this will give Nan for unmatched value