import pandas as pd
import numpy as np
data = {
'Name':['Saurabh','Ranjan','A','B'],
'Age' :[35,34,29,19],
'Salary' : [140000,3500000,180000,950000]
}
df = pd.DataFrame(data)
df.loc[df.Name=='Saurabh', 'Salary'] = np.nan #Assign null value in column
print(df.isnull().sum()) #This is to find if we have null in dataframe or not. And find the sum of it and this will give exact column where null is present.
print(df.fillna(0)) #this will fill null value to 0