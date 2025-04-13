#!/usr/bin/env python
# coding: utf-8

# In[ ]:


get_ipython().run_cell_magic('file', 'app.py', 'from flask import Flask, jsonify, request\n\napp = Flask(__name__)\n\n\n@app.route(\'/api/v1.0/predict\')\ndef home3():\n    # Funkcja do sprawdzenia, czy wartość jest liczbą zmiennoprzecinkową\n    def get_float_or_zero(value):\n        try:\n            return float(value) \n        except ValueError:\n            return 0.0\n\n    num1 = request.args.get("num1", 0)\n    num2 = request.args.get("num2", 0)\n\n    num1 = get_float_or_zero(num1)\n    num2 = get_float_or_zero(num2)\n\n    result = 1 if (num1 + num2) > 5.8 else 0\n\n    return jsonify({\n        "prediction": result,\n        "features": {\n            "num1": num1,\n            "num2": num2\n        }\n    })\n\nif __name__ == \'__main__\':\n    app.run()\n')

