from src.Fifa23.components.data_conversion import splitter
from src.Fifa23.utils.common import read_yaml
from src.Fifa23.constants import SCHEMA_FILE_PATH
from logs import logger,setup_logging
import pandas as pd

try:
    setup_logging()
    logger.info("Logging setup correctly in %s file",__name__)
except ImportError as e:
    print("Logging file was not imported correctly %s", e)
except Exception as e:
    print("Error found in setup_logging in %s file %s",__name__, e)

class Validator():
    def __init__(self):
        self.X,self.y = splitter(True)
        self.X_df = pd.DataFrame(self.X)
        self.schema = read_yaml(SCHEMA_FILE_PATH)["COLUMNS"]
        self.wrong_column_names = []
        self.wrong_dtypes = []

    def validate_data(self) -> bool:
        """
        Validates the column names and data types of the input DataFrame against the schema defined in `schema.yaml`.

        Checks:
        - All expected columns are present.
        - Each column has the expected data type.

        Returns:
            bool: True if all columns match the schema; False otherwise.
        """
       
        for index,(col,dtype) in enumerate(self.schema.items()):

            if col not in self.X_df.columns:

                invalid_name = f"Column {col} has invalid name {self.X_df.columns[index]}"
                logger.error("Column %s has invalid name %",col,self.X_df.columns[index])
                self.wrong_column_names.append(invalid_name)
                continue
            if dtype != self.X_df[col].dtype:
                    wrong_dtype_col = f'Column {col} has invalid data type -- {self.X_df[col].dtype} --  Expected: {dtype}'
                    logger.error("Column %s has invalid data type -- %s ",col,self.X_df[col].dtype)
                    self.wrong_dtypes.append(wrong_dtype_col)

        if (len(self.wrong_column_names) | len(self.wrong_dtypes)):
            print(self.wrong_column_names)
            print(self.wrong_dtypes)
            return False
        return True 
    
     
    
        

if __name__ == "__main__":
    obj = Validator()
    print(obj.validate_data())



