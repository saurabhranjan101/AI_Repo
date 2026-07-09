#Rows & Column Operations(Add, Update, Delete)
import pandas as pd
data = {
'Name':['Saurabh','Ranjan','A','B'],
'Age' :[35,34,29,19],
'Salary' : [140000,3500000,180000,950000]
}
df = pd.DataFrame(data)

#Add New Columns
df['Team'] = ['CEO','HR','SSE','SE']
print(df)

df['Bonus'] = df['Salary'] * 0.2
print(df)

#Add new rows -- we use loc
df.loc[len(df)] = ['ABC',48,750000,'BM', 15000] #Insert a row after the length of dataframe
print(df)
print(len(df))

#Update value
df.loc[0,'Salary'] = 145000
df.loc[df.Name == 'Saurabh', 'Salary'] = 1500000
print(df)

#Delete Value
print(df.drop(df[df.Name =='ABC'].index)) #Delete Row
print(df.drop('Bonus', axis=1)) #Axis=0 bydefault while deleting rows. For column we give Axis =1. Bydefault inplace = false. If we will make tru then this wil save the changes.
print(df.drop(['Bonus','Team'], axis=1)) #Drop Multiple Column