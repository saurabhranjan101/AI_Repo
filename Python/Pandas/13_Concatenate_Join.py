import pandas as pd
df1 = pd.DataFrame({'ID':[1,2,3],'Name':['A','B','C']})
print(df1)

df2 = pd.DataFrame({'ID':[1,2,2,4],'Score':[86,96,77,79]}) 
print(df2)

print(pd.concat([df1,df2], axis=0)) #vertical/row level join

print(pd.concat([df1,df2], axis=1)) #Horizontal/column level

print(pd.merge(df1, df2, how='inner', on='ID'))#Inner join on common column ID

print(pd.merge(df1, df2, how='inner', left_on='ID', right_on= 'ID'))