from flask import Flask, render_template, request
import numpy as np
import pickle

app = Flask(__name__)
model = pickle.load(open('heart_model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        features = [float(x) for x in request.form.values()]
        input_data = np.array(features).reshape(1, -1)
        prediction = model.predict(input_data)

        if prediction[0] == 1:
            return render_template('result.html', result='Heart Failure Detected', alert=True)
        else:
            return render_template('result.html', result='Heart is Healthy', alert=False)
    except:
        return render_template('index.html', error="Please enter valid numeric inputs.")

if __name__ == '__main__':
    app.run(debug=True)
