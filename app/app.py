
# from flask import Flask, request, render_template
# import joblib
# import numpy as np
# import sys
# import os

# # sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))


# from preprocess import preprocess

# app = Flask(__name__)

# model_path = os.path.join(os.path.dirname(__file__), "..", "src", "model.pkl")
# model = joblib.load(model_path)

# @app.route("/", methods=["GET"])
# def index():
#     return render_template("index.html")

# @app.route("/predict", methods=["POST"])
# def predict():
#     try:
#         print("Predict route hit!")
#         age = float(request.form["age"])
#         cholesterol = float(request.form["cholesterol"])
#         print(f"Inputs: age={age}, cholesterol={cholesterol}")

#         features = preprocess(np.array([[age, cholesterol]]))
#         prediction = model.predict(features)[0]
#         result = "High Risk" if prediction == 1 else "Low Risk"

#         return render_template("result.html", result=result, age=age, cholesterol=cholesterol)
#     except Exception as e:
#         print(f"Error during prediction: {e}")
#         return render_template("index.html", result=f"Error: {str(e)}")





# if __name__ == "__main__":
#     app.run(host="0.0.0.0", port=5000, debug=True)


from flask import Flask, render_template, request, jsonify
import numpy as np
import joblib
import os

app = Flask(__name__)
    
model_path = os.path.join(os.path.dirname(__file__), "..", "src", "model.pkl")
model = joblib.load(model_path)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        if request.is_json:
            data = request.get_json()
            age = float(data['age'])
            cholesterol = float(data['cholesterol'])
        else:
            age = float(request.form['age'])
            cholesterol = float(request.form['cholesterol'])

        # Prepare features
        features = np.array([[age, cholesterol]])
        prediction = model.predict(features)
        risk = int(prediction[0])

        if request.is_json:
            # Return JSON response for API calls
            return jsonify({'risk': risk})
        else:
            # Render result page for form submissions
            return render_template('result.html', age=age, cholesterol=cholesterol, risk=risk)

    except Exception as e:
        error_msg = str(e)
        if request.is_json:
            return jsonify({'error': error_msg}), 400
        else:
            return render_template('index.html', error=error_msg)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
