from src.Fifa23.components.data_transformation import data_transform_df
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline,make_pipeline
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from logs import logger,setup_logging


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
    return pipefinal



def create_X_y(df):
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
    return (X,y)

def splitting_data(X,y):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)
    return (X_train, X_test, y_train, y_test)
def splitter(not_train : bool):

    df = data_transform_df()
    X,y = create_X_y(df)
    if not_train:
        return X,y
    X_train, X_test, y_train, y_test = splitting_data(X,y)
    col_transformer = pipelines()
    X_train, X_test, y_train, y_test 
    X_train_transformed = col_transformer.fit_transform(X_train)
    X_test_transformed = col_transformer.transform(X_test)
    return X_train_transformed,X_test_transformed
if __name__ == "__main__":
    splitter(True)
    