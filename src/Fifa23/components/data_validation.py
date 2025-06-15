from src.Fifa23.components.data_conversion import splitter
from src.Fifa23.components.data_transformation import data_transform_df
from src.Fifa23.utils.common import read_yaml
from src.Fifa23.constants import SCHEMA_FILE_PATH
import pandas as pd



X,y = splitter(True)
X_df = pd.DataFrame(X)
print(X_df.info)
columns = read_yaml(SCHEMA_FILE_PATH)["COLUMNS"]
print(columns)

missing_type = [types for types in columns.values() ]

columns = [col for col in X_df.columns]
z = 0
if len(missing_type) == len(columns):
    for i,x in zip(missing_type,columns):
            if X_df.loc[:,x].dtype == i:
                print("Hurray")
                z = z + 1
            print(X_df.loc[:,x].dtype)
            print(i)
            if i[0] == x:
                print(type(X_df.loc[:,x]))
                print(i[1])
                if type(X_df.loc[:,x]) == i[1]:
                    print("Sucess")
print(z)
