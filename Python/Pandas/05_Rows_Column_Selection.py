#Rows & Columns - Selection
#select column
import pandas as pd
data = {
'Name':['Saurabh','Ranjan','A','B'],
'Age' :[35,34,29,27],
'Salary' : [140000,3500000,180000,950000]
}
df = pd.DataFrame(data)
#Select Column
# print(df[['Name']])
# print(df[['Name','Salary']])

# #Rows Selection
# print(df.loc[df.Name == 'Saurabh'])

print(df)
print("=============")
print("=============")
print(df[["Name"]]) # this is to diplay a column.
print(df[["Name","Age","Salary"]])
print("=============")
print("=============")
#Now to display rows
print(df.loc[df.Name == "Saurabh"])
print(df.loc[(df.Name == "Saurabh") & (df.Salary > 15000)])
print("=============")
print("=============")
print(df.iloc[0]) #Index value based
print(df.iloc[0:3]) #[start:stop:step]


print(df.loc[0:2])