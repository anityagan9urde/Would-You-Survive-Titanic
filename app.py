import numpy as np
import pandas as pd
from flask import Flask, request, jsonify, render_template
import joblib
import json

app = Flask(__name__)
regressor = joblib.load('model.pkl')

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict',methods=['GET','POST'])
def predict():
    d = None
    if request.method == 'POST':
        print('POST received')
        d = request.form.to_dict()
    else:
        print('GET received')
        d = request.args.to_dict()

    if regressor:
        whole_table = pd.DataFrame([d])
        object_table = whole_table[whole_table.columns.drop('Age')]
        ohe = pd.get_dummies(object_table)
        query = whole_table[whole_table.columns.drop('Sex', 'Embarked')].append(ohe).fillna(0)
        query = query.reindex(columns=model_columns, fill_value=0)
        prediction = regressor.predict(query)
        if prediction[0]>prediction[1]:
            output = 'would have died.'
        elif prediction[0]<prediction[1]:
            output = 'would have survived.'

        return render_template('index.html', prediction_text='You {}'.format(output))


    else:
        print('Train the model first')
        return ('No model here to use')

if __name__ == "__main__":
    regressor = joblib.load("model.pkl")
    model_columns = joblib.load("model_columns.pkl")
    app.run(debug=True)
