import pandas as pd
data = {
'Name':['Saurabh','Ranjan','A','B'],
'Age' :[35,34,29,19],
'Salary' : [140000,3500000,180000,950000]
}
df = pd.DataFrame(data)
print(df.sort_values('Salary')) #Ascending order
print(df.sort_values('Salary', ascending= False)) #Ascending order