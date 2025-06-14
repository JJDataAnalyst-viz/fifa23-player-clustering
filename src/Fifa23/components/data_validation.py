from src.Fifa23.components.data_conversion import splitter
from src.Fifa23.components.data_transformation import data_transform_df
from src.Fifa23.utils.common import read_yaml
from src.Fifa23.constants import SCHEMA_FILE_PATH

X,y = splitter(True)

columns = read_yaml(SCHEMA_FILE_PATH)["COLUMNS"]
print(columns)

missing_type = [types for types in columns.values() ]
