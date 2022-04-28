from flask import Flask, render_template, request
import requests
import joblib
import numpy as np
import pandas as pd


app = Flask(__name__)
model = joblib.load('model.pkl')

@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')

@app.route('/item-list', methods=['GET'])
def item_list():
    if request.method == 'GET':

        df = pd.read_csv('output_market_basket.csv')

        output = list(df['antecedents'].unique())

        return {"item_list":output}
    else:
        return {"item_list":[]}



@app.route('/predict', methods=['GET'])
def predict():
    Fuel_Type_Diesel = 0
    if request.method == 'GET':
        item = request.args.get('item')

        df = pd.read_csv('output_market_basket.csv')
        df1 = df[['antecedents', 'consequents', 'support','confidence','lift']]

        df2 = df1.loc[df['antecedents'] == item]
        df2 = df2.sort_values(by='lift', ascending=False)

        data = df2.to_dict('records')

        temp = []
        final_op = []

        for i in data:
            if i.get('consequents') in temp:
                continue
            final_op.append(i)

            if len(final_op) > 4:
                break

        return {"data":final_op}
    else:
        return []

if __name__=="__main__":
    app.run(debug=True)