import streamlit as st
import requests

st.title("Previsão de Preço de Casas")

# Formulário para inserir dados da casa
tamanho = st.number_input("Área (sqft_living)", min_value=500, max_value=10000, step=50)
quartos = st.number_input("Número de Quartos", min_value=1, max_value=10)
banheiros = st.number_input("Número de Banheiros", min_value=1, max_value=10)
idade = st.number_input("Idade da Casa (anos)", min_value=0, max_value=100)

# Botão para fazer a previsão
if st.button("Prever Preço"):
    # Montar o JSON com os dados
    dados = {
        "sqft_living": tamanho,
        "bedrooms": quartos,
        "bathrooms": banheiros,
        "idade": idade
    }

    # Enviar os dados para a API
    url = 'http://127.0.0.1:5000/prever'  # Endereço da API (localmente, se estiver rodando localmente)
    resposta = requests.post(url, json=dados)

    # Verificar a resposta e mostrar o preço
    if resposta.status_code == 200:
        preco = resposta.json()['preco_previsto']
        st.write(f"O preço estimado da casa é: {preco}")
    else:
        st.write("Erro na previsão. Verifique os dados ou tente novamente.")
