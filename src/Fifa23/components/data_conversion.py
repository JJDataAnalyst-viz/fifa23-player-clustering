from src.Fifa23.components.data_transformation import data_transform_df
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline, make_pipeline
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer

df = data_transform_df()
scaler = StandardScaler()
encoder = OneHotEncoder(handle_unknown="ignore", sparse_output=False)
df_fifa_str = ["Nationality", "Club"]
df_fifa_num = [
    "Age",
    "Contract Valid Until",
    "Height",
    "Weight",
    "Release Clause",
    "month",
    "year",
]

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
    if not_train:
        X,y = create_X_y(df)
        return X,y
    else:
        X_train, X_test, y_train, y_test = splitting_data(X,y)
        return ( X_train, X_test, y_train, y_test  )
if __name__ == "__main__":
    splitter(True)
    