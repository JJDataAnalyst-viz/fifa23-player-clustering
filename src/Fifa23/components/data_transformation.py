import pandas as pd
import os
from src.Fifa23.utils.common import read_yaml
from pathlib import Path
import re
from logs import setup_logging, logger
from src.Fifa23.constants import CONFIG_FILE_PATH

try:
    setup_logging()
    logger.info("Logging setup correctly in data_transformation.py file")
except ImportError as e:
    print("Logging file was not imported correctly %s", e)
except Exception as e:
    print("Error found in setup_logging in data_transformation file %s", e)


def load_data(path: Path) -> pd.DataFrame:
    """
    Load a CSV file and return it as a pandas DataFrame.

    Args:
        path (Path): The file path to the CSV file.

    Returns:
        pd.DataFrame: DataFrame containing the loaded data from the CSV file.
    Raises:
        FileNotFoundError: If path to file not found
        UnicodeEncodeError: If encoding of file is invalid
    """
    try:
        data = pd.read_csv(path, encoding="utf-8")
        logger.info("Data is loaded from csv file")
        return data
    except FileNotFoundError as e:
        logger.error("Path to file not found %s!", e)
        return None
    except UnicodeEncodeError as e:
        logger.error("Encoding of file is different %s", e)
        return None


def transform_data(data: pd.DataFrame) -> pd.DataFrame:
    """
    Extract selected important columns from the FIFA 23 dataset into a new DataFrame.

    Args:
        data (pd.DataFrame): The original FIFA 23 dataset containing player information and attributes.

    Returns:
        pd.DataFrame: A new DataFrame containing only the essential columns relevant for further analysis.
    Raises:
        KeyError: If columns are missing
    """

    required_columns = [
        "Age",
        "Nationality",
        "Overall",
        "Potential",
        "Club",
        "Joined",
        "Contract Valid Until",
        "Height",
        "Weight",
        "Release Clause",
    ]
    missing_columns = [col for col in required_columns if col not in data.columns]
    if missing_columns:
        logger.error("Copied data has invalid column names %s", missing_columns)
        raise KeyError(f"The following columns are missing {missing_columns}")
    df = data[required_columns].copy()
    logger.info("Copying usefull columns from fifa23 dataset into new one")
    return df


def create_time_data(
    data: pd.DataFrame, column_name_1: str, column_name_2: str
) -> pd.DataFrame:
    """
    Perform feature engineering on the dataset using predefined data transformation functions.

    Args:
        data (pd.DataFrame): The input dataset to be transformed.

    Returns:
        pd.DataFrame: The transformed dataset with engineered features.

    Raises:
         (KeyError,TypeError,ValueError): If data transformation fail
    """
    try:
        data[column_name_1] = pd.to_datetime(data[column_name_1])
        logger.info("Transform data type of column %s into pd.datetime", column_name_1)
        data["month"] = data[column_name_1].dt.month
        logger.info("Extract month from %s column", column_name_1)
        data["year"] = data[column_name_1].dt.year
        logger.info("Extract year from %s column", column_name_1)
        data[column_name_2] = pd.to_datetime(data[column_name_2], format="mixed")
        data[column_name_2] = data[column_name_2].dt.year
        logger.info(
            "Transform data type of column %s into pd.datetime and extract year",
            column_name_2,
        )
        return data
    except (KeyError, TypeError, ValueError) as e:
        logger.error("Date transformation failed %s", e)
        return None


def replace_char(x):
    """
    Remove all characters from a string except digits (0–9) & dot (.).

     Args:
        x (str): The input string to be cleaned, typically representing numerical values with units (e.g., '180cm', '€100M').

    Returns:
        str: A string containing only numeric characters, decimal points, or pipe symbols (if any).
    Raises:
        PaternError: If regex pattern is invalid
    """
    try:
        return re.sub("[^0-9|.]", "", x)
    except re.PatternError as e:
        logger.error("Pattern for regex is invalid %s", e)
        return None

def re_replace(data: pd.DataFrame) -> pd.DataFrame:
    """
    Clean specific columns in the dataset by removing non-numeric characters.

    This function processes the 'Height', 'Weight', and 'Release Clause' columns,
    stripping out any characters except digits & dots (.).

    Args:
        data (pd.DataFrame): The input DataFrame containing the raw player data.

    Returns:
        pd.DataFrame: A new DataFrame with cleaned 'Height', 'Weight', and 'Release Clause' columns.
    """
    try:
        data.Height = data.Height.map(replace_char)
        data.Weight = data.Weight.map(replace_char)
        data["Release Clause"] = data["Release Clause"].map(
            replace_char, na_action="ignore"
        )
        logger.info("Columns are properly cleaned by regex functions")
        return data
    except (KeyError, ValueError, TypeError) as e:
        logger.error("Invalid map function on specific columns %s", e)
        return None

def finalized_data(data):
    """
    Validate and extract the final set of required columns from the dataset.

    Args:
        data (pd.DataFrame): The input DataFrame to validate and filter.

    Returns:
        pd.DataFrame: A DataFrame containing only the required columns.

    Raises:
        KeyError: If any of the required columns are missing from the input data.
    """
    required_columns = [
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
    missing_columns = [col for col in required_columns if col not in data.columns]
    if missing_columns:
        logger.error("Data has invalid column names %s", missing_columns)
        raise KeyError(f"The following columns are missing {missing_columns}")
    data = data.loc[:, list(required_columns)]
    logger.info("Extracted all important columns for data modeling")
    return data


def data_transform_df() -> pd.DataFrame:
    """
    Orchestrates the full data transformation pipeline.

    Returns:
        pd.DataFrame: A fully cleaned and transformed DataFrame ready for analysis.
    """
    try:
        raw_data = read_yaml(CONFIG_FILE_PATH)["data_transformation"]
        df = load_data(raw_data["raw_data"])
        logger.info("Data sucesfully loaded")
        transformed_df = transform_data(df)
        logger.info("Data sucesfully transformed")
        data_with_time = create_time_data(
            transformed_df, "Joined", "Contract Valid Until"
        )
        logger.info("Sucessfully created datetime columns")
        full_transformed_data = re_replace(data_with_time)
        logger.info("Sucessfully used regex")
        clean_df = finalized_data(full_transformed_data)
        logger.info("Sucessfully extracted columns")
        return clean_df
    except Exception as e:
        logger.error("Data transformation pipeline has failed %s", e)


if __name__ == "__main__":
    data_transform_df()
