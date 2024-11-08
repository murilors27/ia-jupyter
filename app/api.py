from flask import Flask, request, jsonify
import joblib
import numpy as np
import pandas as pd

model = joblib.load('app/modelo_regressao_linear.pkl')

app = Flask(__name__)

@app.route('/prever', methods=['POST'])
def predict():
    data = request.get_json()

    required_fields = ['sqft_living', 'bedrooms', 'bathrooms', 'idade']
    for field in required_fields:
        if field not in data:
            return jsonify({"error": f"Campo '{field}' é obrigatório"}), 400

    try:
        sqft_living = data['sqft_living']
        bedrooms = data['bedrooms']
        bathrooms = data['bathrooms']
        idade = data['idade']
        
        input_data = pd.DataFrame([[sqft_living, bedrooms, bathrooms, idade]], columns=['sqft_living', 'bedrooms', 'bathrooms', 'idade'])
        
        predicted_price = np.expm1(model.predict(input_data))[0]

        # Formatar o preço com R$ e 2 casas decimais
        formatted_price = f"US$ {predicted_price:,.2f}"

        return jsonify({"preco_previsto": formatted_price}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
