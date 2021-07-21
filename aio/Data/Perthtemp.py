import pandas as pd
perth_file_path = '../Data/PerthTemperatures.csv'
ptemp_data = pd.read_csv(perth_file_path)
ptemp_data.describe()
print(ptemp_data)