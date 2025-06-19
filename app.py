from flask import Flask, render_template, request, jsonify
from src.Fifa23.utils.common import load_bin
from src.Fifa23.components.data_transformation import data_transform_df
from pathlib import Path
import subprocess
import pandas as pd
from flask import jsonify
app = Flask(__name__)
df = data_transform_df()

# Load or retrain model and transformer
if Path("models/model.pkl").exists() and Path("models/transformer.pkl").exists():
    model = load_bin("models/model.pkl")
    transformation = load_bin("models/transformer.pkl")
else:
    subprocess.run(["python", "-m", "main"])
    model = load_bin("models/model.pkl")
    transformation = load_bin("models/transformer.pkl")


@app.route("/", methods=["GET", "POST"])
def index():
    nationalities = sorted(df["Nationality"].dropna().unique().tolist())
    clubs = sorted(df["Club"].dropna().unique().tolist())

    if request.method == "POST":
        try:
            input_data = request.form.to_dict()

            # Convert types properly for numeric columns
            for key in ['age', 'contract', 'height', 'weight', 'release', 'month', 'year']:
                val = input_data.get(key)
                if val:
                    if key == 'release':
                        input_data[key] = float(val)
                    else:
                        input_data[key] = int(val)
                else:
                    input_data[key] = None  # or default values

            # Create a single-row DataFrame (transformer expects this)
            df_input = pd.DataFrame([{
                "Age": input_data.get("age"),
                "Nationality": input_data.get("nationality"),
                "Club": input_data.get("club"),
                "Contract Valid Until": input_data.get("contract"),
                "Height": input_data.get("height"),
                "Weight": input_data.get("weight"),
                "Release Clause": input_data.get("release"),
                "month": input_data.get("month"),
                "year": input_data.get("year"),
            }])

            # Apply your transformer and model
            transformed = transformation.transform(df_input)
            prediction = model.predict(transformed)

            return jsonify({"prediction": float(prediction[0])})

        except Exception as e:
            print("Prediction error:", e)
            return jsonify({"error": str(e)}), 500

    # GET request just renders form
    return render_template("index.html", nationalities=nationalities, clubs=clubs)


if __name__ == "__main__":
    app.run(debug=True)
