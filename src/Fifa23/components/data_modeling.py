from src.Fifa23.utils.common import read_yaml,save_bin
from logs import setup_logging, logger
from src.Fifa23.components.data_conversion import splitter
from src.Fifa23.components.data_validation import Validator
from xgboost import XGBRegressor
from src.Fifa23.constants import PARAMS_FILE_PATH
import wandb

try:
    setup_logging()
    logger.info("Logging setup correctly in %s file",__name__)
except ImportError as e:
    print("Logging file was not imported correctly %s", e)
except Exception as e:
    print("Error found in setup_logging in %s file %s", __name__,e)

class XgboostModel():
    def __init__(self):
        self.X_train_transformed,self.X_test_transformed,self.y_train,self.y_test = splitter(False)
        self.validate_data = Validator()
        self.params = read_yaml(PARAMS_FILE_PATH)["xgboost_params"]

        self.run = wandb.init(
            project="Fifa23_Xgboost",
            entity="sciopsengineer-iqfm",
            config=self.params
            
        )

    def xgboost_user(self) -> XGBRegressor:
        """
                Creates, trains, and saves an XGBoost Regressor model.

                This method initializes an `XGBRegressor` with parameters specified in `self.params`, 
                fits it on the training data (`self.X_train_transformed`, `self.y_train`), and performs 
                a prediction on the test set (`self.X_test_transformed`). The trained model is then 
                saved to the `models/model.pkl` file.

                Returns
                -------
                XGBRegressor
                    The trained XGBoost Regressor model.
                
                Raises
                ------
                ValueError
                    If data validation fails via `self.validate_data.validate_data()`.
        """
        if self.validate_data.validate_data():
            xgb = XGBRegressor(**self.params)
            xgb.fit(self.X_train_transformed,self.y_train)
            xgb.predict(self.X_test_transformed)
         
            save_bin(xgb,f"models/model.pkl")
            return xgb
        
    def model_score(self,model,X_test,y_test):
        if XgboostModel.xgboost_user is not None:
            self.run.log({"xgboost_score":model.score(X_test,y_test)})
            


if __name__ == "__main__":
    model = XgboostModel()
    xgb = model.xgboost_user()
    model.model_score(xgb,X_test=model.X_test_transformed,y_test=model.y_test)