# JJDataAnalyst-viz

## Project Overview
JJDataAnalyst-viz is a comprehensive data science project focused on analyzing and modeling player performance data from the FIFA 23 dataset. The project includes data ingestion, cleaning, feature engineering, exploratory data analysis, and building a predictive model to estimate player overall ratings based on various attributes.

This repository provides a clean, modular pipeline leveraging state-of-the-art machine learning techniques to deliver actionable insights and reliable predictions from raw FIFA player data.

---

## Key Features

- **Data Ingestion:** Automated download and management of the FIFA 23 dataset from Kaggle using the `kagglehub` API.  
- **Data Cleaning & Preprocessing:** Handling missing values, extracting features from date columns, and cleaning string-formatted numerical data (e.g., height, weight, release clauses).  
- **Feature Engineering:** Creation of additional features such as joining month/year extracted from contract dates.  
- **Pipeline Construction:** Robust `sklearn` pipeline with separate transformations for categorical and numerical features, including imputers, encoders, and scalers.  
- **Machine Learning Model:** Implementation of an XGBoost regressor to predict players' overall ratings.  
- **Model Evaluation:** Train-test split and performance scoring on unseen data.  
- **Model Persistence:** Saving the final pipeline as a joblib object for easy reuse and deployment.

---

## Dataset
The dataset is the official FIFA 23 player statistics database from Kaggle, containing detailed player attributes such as:

- Age  
- Nationality  
- Club  
- Contract details (joined date, contract validity)  
- Physical attributes (height, weight)  
- Financial data (release clause)  
- Performance metrics (overall rating, potential)  

---

## Project Structure

JJDataAnalyst-viz/
├── data/
│   └── raw/                   # Raw downloaded dataset files
├── models/                    # Saved model pipeline artifacts
│   └── pipeline.joblib
├── src/                       # Source code including data ingestion and preprocessing scripts
├── research/                  # Exploratory data analysis and research notebooks
├── templates/                 # Project templates for consistent structure
├── app.py                    # Flask application for model serving (if applicable)
├── main.py                   # Main script to run the pipeline
├── requirements.txt          # Project dependencies
├── Dockerfile                # Docker configuration for containerized deployment
├── params.yaml               # Parameter configuration file
├── README.md                 # Project overview and instructions
└── .gitignore                # Git ignore rules




## Installation

Clone the repository:
```bash
git clone https://github.com/yourusername/JJDataAnalyst-viz.git
cd JJDataAnalyst-viz
```

```bash
pip install -r requirements.txt
```

# Usage
## Download and Prepare Data
The dataset is downloaded automatically using the kagglehub package and saved to data/raw.

## Run Data Processing and Training
Execute the pipeline to clean data, engineer features, train the model, and save the trained pipeline:


```python
python main.py
```
## Load and Use Model for Predictions
Load the saved pipeline for inference in your scripts or web apps:

```python
import joblib

pipeline = joblib.load("models/pipeline.joblib")
predictions = pipeline.predict(new_data)
```

## Model Details
- Model Type: Gradient Boosting Regressor (XGBoost)

- Features: Mixed categorical and numerical features including player demographics and contract info

- Pipeline: Includes imputation for missing values, encoding for categorical variables, and scaling for numerical data

- Performance: Evaluated on a 30% test split

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request with your improvements.

## License
This project is licensed under the MIT License.