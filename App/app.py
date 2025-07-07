from flask import Flask, render_template, request
import numpy as np
import pandas as pd
import joblib

app = Flask(__name__)

# Load model and scaler
model = joblib.load("model/model.pkl")
scaler = joblib.load("model/scaler.pkl")

# Route for homepage
@app.route("/")
def index():
    return render_template("index.html")

# Route for prediction
@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Extract input values from form
        age = float(request.form["age"])
        sc = float(request.form["sc"])
        hemo = float(request.form["hemo"])
        al = float(request.form["al"])
        bp = float(request.form["bp"])
        sg = float(request.form["sg"])

        # Prepare input as DataFrame with correct feature names
        input_df = pd.DataFrame([[age, sc, hemo, al, bp, sg]],
                                columns=["age", "sc", "hemo", "al", "bp", "sg"])

        # Scale input
        scaled_input = scaler.transform(input_df)

        # Predict using the model
        prediction = model.predict(scaled_input)
        print("Prediction:", prediction)

        # Generate result message
        if prediction[0] == "ckd":
            result = "🔴 The person is likely to have Chronic Kidney Disease (CKD)."
        else:
            result = "🟢 The person is unlikely to have Chronic Kidney Disease."

        return render_template("index.html", result=result)

    except Exception as e:
        print("Error during prediction:", e)
        return render_template("index.html", result=f"⚠️ Error: {str(e)}")

if __name__ == "__main__":
    app.run(debug=True)
