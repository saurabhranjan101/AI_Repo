import pandas as pd
data = {
'Name':['Saurabh','Monu','Priyanka','Soni'],
'Age' :[16,26,13,25],
'Salary' : [25000,26000,24500,29000]
}
df = pd.DataFrame(data)
print(df)
print(type(df))