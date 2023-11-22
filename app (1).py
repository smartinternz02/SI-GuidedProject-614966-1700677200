from flask import Flask, request, render_template
import pickle
import numpy as np
import pandas as pd
import os

app = Flask(__name__, template_folder=r'C:\Users\Hitha\OneDrive\Desktop\Templates')

# Use relative paths for better portability
pickle_file_path = r'c:\Users\Hitha\OneDrive\Desktop\Templates\random.pkl'

with open(pickle_file_path, 'rb') as file:
    random = pickle.load(file)

# You might need to load the scaler used during training here if any

@app.route("/")
def f():
    return render_template("hhmr.html")

@app.route("/inspect")
def inspect():
    return render_template("home.html")

@app.route("/predict", methods=["POST"])
def predict():
    predict = None
    if request.method == 'POST':
        # Convert form data to float
        features = {
            "yummy": float(request.form["yummy"]) if request.form["yummy"].strip() != '' else 0.0,
            "convenient": float(request.form["convenient"]) if request.form["convenient"].strip() != '' else 0.0,
            "spicy": float(request.form["spicy"]) if request.form["spicy"].strip() != '' else 0.0,
            "fattening": float(request.form["fattening"]) if request.form["fattening"].strip() != '' else 0.0,
            "greasy": float(request.form["greasy"]) if request.form["greasy"].strip() != '' else 0.0,
            "fast": float(request.form["fast"]) if request.form["fast"].strip() != '' else 0.0,
            "cheap": float(request.form["cheap"]) if request.form["cheap"].strip() != '' else 0.0,
            "tasty": float(request.form["tasty"]) if request.form["tasty"].strip() != '' else 0.0,
            "expensive": float(request.form["expensive"]) if request.form["expensive"].strip() != '' else 0.0,
            "healthy": float(request.form["healthy"]) if request.form["healthy"].strip() != '' else 0.0,
            "disgusting": float(request.form["disgusting"]) if request.form["disgusting"].strip() != '' else 0.0,
            "Like": float(request.form["Like"]) if request.form["Like"].strip() != '' else 0.0,
            "Age": float(request.form["Age"]) if request.form["Age"].strip() != '' else 0.0,
            "Gender": float(request.form["Gender"]) if request.form["Gender"].strip() != '' else 0.0,
        }



        # Create a DataFrame with named columns
        features_df = pd.DataFrame([features])
        
        try:
            predict_data = features_df.values
            predict = random.predict(predict_data)
        except Exception as e:
            print(f"Prediction error: {e}")

        if np.array_equal(predict, [0]):
            return render_template('hhmr.html', predict="Predicts Customer belongs to cluster 0")

        elif np.array_equal(predict, [1]):
            return render_template('hhmr.html', predict="Predicts Customer belongs to cluster 1")

        elif np.array_equal(predict, [2]):
            return render_template('hhmr.html', predict="Predicts Customer belongs to cluster 2")
        
        elif np.array_equal(predict, [3]):
            return render_template('hhmr.html', predict="Predicts Customer belongs to cluster 3")
        
        elif np.array_equal(predict, [4]):
            return render_template('hhmr.html', predict="Predicts Customer belongs to cluster 4")
        
        else:
             return render_template('hhmr.html', predict="Predicts Customer belongs to cluster 5")

        
        
        
        return render_template("hhmr.html")

if __name__ == "__main__":
    app.run(debug=True)
