# app.py
from flask import Flask, render_template, request
import pickle
import numpy as np
import pandas as pd

app = Flask(__name__)
app.secret_key = "replace-this-with-a-secure-key"

# Load artifacts (model.pkl and scaler.pkl should be in project root)
model = pickle.load(open("model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))

# Optional: load dataset for providing defaults / dropdowns
try:
    sales_df = pd.read_csv("monthly_sales.csv")
    stores = sorted(sales_df['store_id'].unique().tolist())
except Exception:
    sales_df = None
    stores = list(range(1,11))  # fallback

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    inputs = None
    if request.method == "POST":
        try:
            # Read inputs
            store_id = int(request.form.get("store_id"))
            year = int(request.form.get("year"))
            month = int(request.form.get("month"))
            promo = int(request.form.get("promo"))
            prev_month_sales = float(request.form.get("prev_month_sales"))

            feat = np.array([[store_id, year, month, promo, prev_month_sales,
                              np.sin(2 * np.pi * month / 12),
                              np.cos(2 * np.pi * month / 12)]])

            feat_scaled = scaler.transform(feat)
            pred = model.predict(feat_scaled)[0]
            prediction = round(float(pred), 2)
            inputs = {
                "store_id": store_id,
                "year": year,
                "month": month,
                "promo": promo,
                "prev_month_sales": prev_month_sales
            }
        except Exception as e:
            prediction = f"Error: {e}"

    # Provide some UI helpers
    return render_template("index.html", prediction=prediction, inputs=inputs, stores=stores)

if __name__ == "__main__":
    app.run(debug=True)
