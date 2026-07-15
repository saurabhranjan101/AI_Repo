import pandas as pd
data = {
'Name':['Saurabh','Ranjan','A','B'],
'Age' :[35,34,29,19],
'Salary' : [140000,3500000,180000,950000]
}
df = pd.DataFrame(data)
df['DOJ'] = ['2024-01-01','2024-01-15','2024-03-28','2024-03-03'] #Adding a new column

#first convert DOJ in date time datatype
df['DOJ'] = pd.to_datetime(df['DOJ'])
#print(df.dtypes)

#Extract Year, Month and day in seperate field & adding seperate column
df['Year'] = df['DOJ'].dt.year
df['Month'] = df['DOJ'].dt.month
df['Day'] = df['DOJ'].dt.day
print(df)

#Now apply aggregation & group by here.
print(df['Month'].value_counts())
#Count for January
print(df[df['Month'] ==1].value_counts())

#groupby
print(df.groupby('Month')['Salary'].sum()) #Sum of salary per month
print(df.groupby('Month')['Salary'].mean()) #Average salary per month
print(df.groupby('Month').agg({'Salary':'mean', 'Name':'count'}))