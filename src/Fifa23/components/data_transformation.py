import pandas as pd
import os
from src.Fifa23.utils.common import read_yaml 
from pathlib import Path
import re

def load_data(path : Path) -> pd.DataFrame:
    data =  pd.read_csv(path,encoding="utf-8")
    print(data.columns)
    return data

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