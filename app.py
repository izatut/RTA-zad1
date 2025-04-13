#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/api/v1.0/predict')
def home3():
    # Funkcja do sprawdzenia, czy wartość jest liczbą zmiennoprzecinkową
    def get_float_or_zero(value):
        try:
            return float(value) 
        except ValueError:
            return 0.0

    num1 = request.args.get("num1", 0)
    num2 = request.args.get("num2", 0)

    num1 = get_float_or_zero(num1)
    num2 = get_float_or_zero(num2)

    result = 1 if (num1 + num2) > 5.8 else 0

    return jsonify({
        "prediction": result,
        "features": {
            "num1": num1,
            "num2": num2
        }
    })

if __name__ == '__main__':
    app.run()

