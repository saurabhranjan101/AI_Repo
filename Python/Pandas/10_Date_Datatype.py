import pandas as pd
data = {
'Name':['Saurabh','Ranjan','A','B'],
'Age' :[35,34,29,19],
'Salary' : [140000,3500000,180000,950000]
}
df = pd.DataFrame(data)
df['DOJ'] = ['2024-01-01','2024-01-15','2024-03-28','2024-03-03']
df['DOJ'] = pd.to_datetime(df['DOJ'])
print(df.dtypes)
df['Year'] = df['DOJ'].dt.year
df['Month'] = df['DOJ'].dt.month
df['Day'] = df['DOJ'].dt.day
print(df)

df['DOJ'] +pd.Timedelta(days=90)



# df['DOJ'] = pd.to_datetime(df['DOJ']) #Converting into datetime datatype
# print(df.dtypes) #print datatype
# df1 = df
# df1['DOJ2'] = ['01-01-2025','15-01-2025','28-03-2025','03-03-2025']
# print(df1)
# df1['DOJ2'] = pd.to_datetime(df1['DOJ2'], format='%d-%m-%Y', errors='coerce')
# print(df1.dtypes)
# print(df1)
# df = df.drop('DOJ2', axis = 1)
# print(df)
# df['Year'] = df['DOJ'].dt.year #this is to extract year
# df['Month'] = df['DOJ'].dt.month #this is to extract month
# df['Day'] = df['DOJ'].dt.day ##this is to extract day
# print(df)