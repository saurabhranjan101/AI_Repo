import pandas as pd
print(pd.__version__) ##this is to check pandas version

#Create Dataframe
df = pd.DataFrame([11,22,33], columns=['Column_Name'])
print(df)
print(type(df))