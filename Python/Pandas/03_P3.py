#Basic Dataframe Understanding
# df.head() #top rows -- bydefault 5
import pandas as pd
data = {
'Name' : ['Saurabh','Monu','Priyanka','Soni'],
'Age' :[16,26,13,25],
'Salary' : [25000,26000,24500,29000]
}
df = pd.DataFrame(data)
print(df.head(2))
print(df.tail(2))
print(df.shape)
print(df.columns)
df.rename(columns={'Salary':'Monthly_Salary'}, inplace= True) #this rename column name and inplace = true saves the updated column name
print(df)
print("------------------")
df.info() #Gives info of the dataframe
print("=======================")
print(df.describe())