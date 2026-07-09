import pandas as pd
data = {
'Name':['Saurabh','Ranjan','A','B'],
'Age' :[35,34,29,19],
'Salary' : [140000,3500000,180000,950000]
}

df = pd.DataFrame(data)
print(df)
#loc & iloc
print(df.loc[(df.Name == 'Saurabh') | ((df.Age > 30))])
print(df["Name"])
print(df.loc[0:2])

#iloc
print(df.iloc[0])
print(df.iloc[0:2])