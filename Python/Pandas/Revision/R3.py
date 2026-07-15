# import pandas as pd
# data = {
# 'Name':['Saurabh','Ranjan','A','B'],
# 'Age' :[35,34,29,19],
# 'Salary' : [140000,3500000,180000,950000]
# }
# df = pd.DataFrame(data)
# print(df[['Name','Age']])
# #Apply filter on Name Colum
# print(df.loc[(df.Name == "Saurabh") | (df.Salary > 150000)])
# print(df.loc[0:2])
# print(df.iloc[0:2])
#Print all rows for age >20
# print(df[df.Age > 20])
# #where condition
# print(df.where(df.Age > 20))


import pandas as pd
data = {
'Name':['Saurabh','Ranjan','A','B'],
'Age' :[35,34,29,19],
'Salary' : [140000,3500000,180000,950000]
}
df = pd.DataFrame(data)
#Let's add, update and Delete values from dataframe

#Add New Column
df['Designation'] = ['OE','SOPE','Lead','PM']
df['Bonus'] = df.Salary * 0.2
# print(df)

#Add New Row - we will use loc
df.loc[len(df)] = ['C',39,125000,'AOE', 25000]
df.loc[len(df)] = ['D',21, 138000, 'SRE', 26000]
df.loc[len(df)] = ['E',23, 128000, 'SSRE', 29000]
print(df)

#Update Value
df.loc[5,'Salary'] = 148000 #go to index 5 and on salary update the value to 148000
df.loc[df.Name == 'Saurabh', 'Designation'] = 'Senior IT OPS Engineer'
# print(df)

#Delete
print(df.drop(df[df.Name == 'D'].index)) #Drop row of name D for the index value
print(df.drop(df[df.Name == 'E'].index)) #Drop row of name E for the index value

#Column Drop
print(df.drop('Bonus', axis = 1)) #Drop Column
print(df.drop(['Designation','Bonus'], axis =1))  #Drop multiple Columns