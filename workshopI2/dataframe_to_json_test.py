# Program: create a dataframe and export it to a JSON file + CSV file (just in case)

import os
import pandas as pd

#def create_directory(dir_name):
#    try:
#        os.mkdir(dir_name)
#        return 'Output JSON directory successfully created'
#    except:
#        return 'Error while creating the output JSON directory'

data_frame =  {
    'Car': ['Ford Fiesta ST', 'Alfa Romeo 2000', 'Alfa Romeo Guilietta', 'Audi A5', 'Chevrolet Camaro'],
    'Body Style': ['3 to 5Door Hatchback','4Door saloon','5Door Hatchback','2Door coupe or 5Door liftback','2Door coupe or convertible'],
    'Transmission': ['6speed manual','5speed manual','6speed manual or Dual Dry Clutch', '6speed manual','6speed manual']
    }

df = pd.DataFrame(data_frame, columns=['Car','Body Style','Transmission'])

print(df)

new_json_file = os.path.join(os.getcwd(), 'cars_data_2.json')
new_csv_file = os.path.join(os.getcwd(), 'cars_data.csv')

df.to_json(new_json_file)
df.to_csv(new_csv_file)

df_read = pd.read_json('cars_data.json')

print(df_read)

# lister les fichiers JSON dans le répertoire de sortie
for file_name in os.listdir(os.getcwd()):
    if file_name.endswith('.json') or file_name.endswith('.csv'):
        print(file_name)
