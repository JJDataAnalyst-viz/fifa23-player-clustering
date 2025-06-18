from src.Fifa23.components.data_transformation import data_transform_df
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline,make_pipeline
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from logs import logger,setup_logging
from src.Fifa23.utils.common import save_bin
import numpy as np
import pandas as pd

try:
    setup_logging()
    logger.info("Logging setup correctly in data_conversion file")
except ImportError as e:
    print("Logging file was not imported correctly %s", e)
except Exception as e:
    print("Error found in setup_logging in data_conversion file %s", e)



df = data_transform_df() # Use transformed dataset
scaler = StandardScaler()  
encoder = OneHotEncoder(handle_unknown="ignore", sparse_output=False) # New nationality or club will be ignored in test dataset 


df_fifa_str = ["Nationality", "Club"] # Columuns for string pipeline
df_fifa_num = [                       # Columns for numerical pipeline                  
    "Age",
    "Contract Valid Until",
    "Height",
    "Weight",
    "Release Clause",
    "month",
    "year",
]

def pipelines():
    '''
    Create a preprocessing pipeline for transforming categorical and numerical features.

    Returns:
    sklearn.pipeline.Pipeline
    '''

    str_pipeline = Pipeline(
        steps=[
            ("SimpleImputer", SimpleImputer(strategy="most_frequent")),
            ("OneHotEncoder", encoder),
        ]
    )

    num_pipeline = Pipeline(
        steps=[
            ("SimpleImputer", SimpleImputer(strategy="mean")),
            ("StandardScaler", scaler),
        ]
    )

    col_transformer = ColumnTransformer(
        transformers=[
            ("str_pipeline", str_pipeline, df_fifa_str),
            ("num_pipeline", num_pipeline, df_fifa_num),
        ],
        remainder="drop",
        n_jobs=-1,
    )

    pipefinal = make_pipeline(col_transformer)
    logger.info("Created pipeline for transformation string data and numerical data")
    return pipefinal



def create_X_y(df) -> tuple[pd.DataFrame,np.array]:
    '''
    Splits the input DataFrame into features (X) and target (y).


    Parameters
    ----------
    df : pd.DataFrame
        The input DataFrame containing both features and target.

    Returns
    -------
    tuple[pd.DataFrame, pd.Series]
        X: Feature matrix with selected columns.
        y: Target variable (last column of the DataFrame).
    '''
    X = df.loc[
        :,
        [
            "Age",
            "Nationality",
            "Club",
            "Contract Valid Until",
            "Height",
            "Weight",
            "Release Clause",
            "month",
            "year",
        ],
    ]
    y = df.iloc[:, -1]
    logger.info("Split dataframe into X and y")
    return (X,y)



def splitting_data(X : pd.DataFrame,y : np.array) -> tuple[pd.DataFrame,pd.DataFrame,np.array,np.array]:
    '''
    Split X,y data into train and test dataset

    Parameters
    -----
    X : pd.DataFrame
        Training and testing dataset
    y : np.array
        Outcome 

    Returns
    -------
    tuple
        A tuple containing the split data:
    
    - X_train : pd.DataFrame
        Training feature data.
    - X_test : pd.DataFrame
        Testing feature data.
    - y_train : pd.Series
        Training target values.
    - y_test : pd.Series
        Testing target values.
    '''
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)
    logger.info("Split X and y into training and testing data")
    return (X_train, X_test, y_train, y_test)


def splitter(not_train : bool):
    """
    Split and optionally transform data for training/testing or just return raw features and target.

    If `not_train` is True, returns the raw feature matrix (X) and target vector (y).
    If False, it splits the data into train/test sets and applies preprocessing transformations.

    Parameters
    ----------
    not_train : bool
        - True: Return raw (X, y)
        - False: Return transformed training and test sets

    Returns
    -------
    tuple
        If not_train is True:
            - X : pd.DataFrame 
                Feature matrix before transformation
            - y : pd.Series
                Target vector
        If not_train is False:
            - X_train_transformed : np.ndarray
                Transformed training features
            - X_test_transformed : np.ndarray
                Transformed testing features
            - y_train : pd.Series
                Training labels
            - y_test : pd.Series
                Testing labels
    """
    df = data_transform_df()
    X,y = create_X_y(df)

    if not_train:
        logger.info("Using only X,y ")
        return X,y
    
    X_train, X_test, y_train, y_test = splitting_data(X,y)
    col_transformer = pipelines()
    X_train, X_test, y_train, y_test 
    X_train_transformed = col_transformer.fit_transform(X_train)
    X_test_transformed = col_transformer.transform(X_test)
    save_bin(col_transformer,"models/transformer.pkl")
    return X_train_transformed,X_test_transformed,y_train,y_test


if __name__ == "__main__":
    splitter(True)
    