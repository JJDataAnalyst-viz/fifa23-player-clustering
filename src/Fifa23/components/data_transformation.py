import pandas as pd
import os
from src.Fifa23.utils.common import read_yaml 
from pathlib import Path
import re
from logs import setup_logging,logger

try:
    setup_logging()
    logger.info("Logging setup correctly in data_transformation.py file")
except ImportError as e:
    print("Logging file was not imported correctly %s", e)
except Exception as e:
    print("Error found in setup_logging in data_transformation file %s", e)

def load_data(path : Path) -> pd.DataFrame:
    '''
        Load a CSV file and return it as a pandas DataFrame.

        Args:
            path (Path): The file path to the CSV file.

        Returns:
            pd.DataFrame: DataFrame containing the loaded data from the CSV file.
    '''
    try :
        data =  pd.read_csv(path,encoding="utf-8")
        logger.info("Data is loaded from csv file")
        return data
    except FileNotFoundError as e:
         logger.error("Path to file not found %s!",e)
def transform_data(data : pd.DataFrame):
    
    df = data[["Age",
        "Nationality",
        "Overall",
        "Potential",
        "Club",
        "Joined",
        "Contract Valid Until",
        "Height",
        "Weight",
        "Release Clause"]].copy()
    
    return df

def create_time_data(data):
    data["Joined"] = pd.to_datetime(data["Joined"])
    data["month"] = data.Joined.dt.month
    data["year"] = data.Joined.dt.year
    data["Contract Valid Until"] = pd.to_datetime(
    data["Contract Valid Until"], format="mixed"
    )
    data["Contract Valid Until"] = data["Contract Valid Until"].dt.year
    return data

def replace_char(x):
        return re.sub("[^0-9|.]", "", x)


def re_replace(data):
        data.Height = data.Height.map(replace_char)
        data.Weight = data.Weight.map(replace_char)
        data["Release Clause"] = data["Release Clause"].map(
            replace_char, na_action="ignore"
        )
        return data

def finalized_data(data):
        columns_list = [
        "Age",
        "Nationality",
        "Club",
        "Joined",
        "Contract Valid Until",
        "Height",
        "Weight",
        "Release Clause",
        "month",
        "year",
        "Potential",
        "Overall",
        ]
        data = data.loc[:, columns_list]
        return data


def data_transform_df():
     df =  load_data("data/raw/35/FIFA23_official_data.csv")
     transformed_df = transform_data(df)
     data_with_time = create_time_data(transformed_df)
     full_transformed_data = re_replace(data_with_time)
     clean_df = finalized_data(full_transformed_data)
     return clean_df


if __name__ == "__main__":
    data_transform_df()