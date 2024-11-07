from flask import Flask, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)

# Carregando o modelo treinado
model = joblib.load('app/modelo_regressao_linear.pkl')


@app.route('/prever', methods=['POST'])
def prever():
    # Obtendo dados da requisição
    dados = request.get_json()

    # Extraindo características
    tamanho = dados.get('sqft_living')
    quartos = dados.get('bedrooms')
    banheiros = dados.get('bathrooms')
    idade = dados.get('idade')

    # Preparando os dados para a previsão
    entrada = np.array([[tamanho, quartos, banheiros, idade]])

    # Fazendo a previsão
    preco_previsto = model.predict(entrada)

    # Formatar o preço previsto em reais
    preco_formatado = f"R$ {preco_previsto[0]:,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.')

    # Retornando o resultado formatado
    return jsonify({'preco_previsto': preco_formatado})


if __name__ == '__main__':
    app.run(debug=True)