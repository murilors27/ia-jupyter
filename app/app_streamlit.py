import streamlit as st
import requests

# Função para realizar a previsão via API Flask
def previsao_preco(sqft_living, bedrooms, bathrooms, idade):
    url = "http://127.0.0.1:5000/prever"  # URL da API Flask local
    dados = {
        'sqft_living': sqft_living,
        'bedrooms': bedrooms,
        'bathrooms': bathrooms,
        'idade': idade
    }
    response = requests.post(url, json=dados)
    
    if response.status_code == 200:
        data = response.json()
        return data.get('preco_previsto', 'Erro ao obter o preço')
    else:
        return "Erro ao obter a previsão. Verifique os dados ou tente novamente."

# Interface do Streamlit
st.title('Previsão de Preço de Casas')

# Inputs de dados
sqft_living = st.number_input('Área (sqft_living)', min_value=100, max_value=10000, value=500)
bedrooms = st.number_input('Número de Quartos', min_value=1, max_value=10, value=1)
bathrooms = st.number_input('Número de Banheiros', min_value=1, max_value=10, value=1)
idade = st.number_input('Idade da Casa (anos)', min_value=0, max_value=100, value=0)

# Botão para fazer a previsão
if st.button('Prever Preço'):
    preco_estimado = previsao_preco(sqft_living, bedrooms, bathrooms, idade)
    st.write(f'O preço estimado da casa é: {preco_estimado}')
