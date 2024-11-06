# Análise de Preços de Casas

Este projeto realiza uma análise de dados de preços de casas e disponibiliza uma API para previsão de preços, utilizando aprendizado de máquina.

## Dependências

Todas as dependências do projeto estão listadas no arquivo `requirements.txt`.

### Instalação das Dependências

Para instalar as dependências, execute o seguinte comando no terminal:

pip install -r requirements.txt

## Como Executar:

O notebook analise_dados.ipynb contém a análise exploratória e o treinamento do modelo de regressão linear. Abra-o para ver o processo de análise de dados e criação do modelo.

## Executando a API:

A API foi criada utilizando Flask. Ela permite fazer previsões do preço de uma casa com base nos atributos fornecidos.
Para iniciar a API, no diretório app/, execute:
python app/api.py

A API estará disponível em http://127.0.0.1:5000.

## Endpoints da API
POST /predict
Endpoint para prever o preço da casa.
Parâmetros esperados no corpo da requisição (JSON):

sqft_living: Área em pés quadrados.
bedrooms: Número de quartos.
bathrooms: Número de banheiros.
idade: Idade do imóvel (em anos).

Exemplo de Requisição:
POST /predict
{
    "sqft_living": 2000,
    "bedrooms": 3,
    "bathrooms": 2,
    "idade": 10
}
