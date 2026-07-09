import pandas as pd
data = {
'Name':['Saurabh','Ranjan','A','B'],
'Age' :[35,34,29,27],
'Salary' : [140000,3500000,180000,950000]
}
df = pd.DataFrame(data)
#loc is a row based attribute of pandas
print(df.loc[df.Name == "Ranjan"])
print(df.loc[(df.Name == "Ranjan") & (df.Age >= 30)])
print(df.loc[0:2])

#iloc - index based attribute in pandas
print(df.iloc[0]) #This displays only zeroth row
print(df.iloc[0:3]) #this is n-1