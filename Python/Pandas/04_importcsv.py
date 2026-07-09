#Save & Load data from csv
import pandas as pd
data = {
'Name' : ['Saurabh','Monu','Priyanka','Soni'],
'Age' :[16,26,13,25],
'Salary' : [25000,26000,24500,29000]
}
df = pd.DataFrame(data)
#To save data in CSV format
df.to_csv('Test_data.csv', index= False) #Save file in CSV format without index
df_load = pd.read_csv('Test_data.csv') #load content of csv file into a variable
print(df_load)