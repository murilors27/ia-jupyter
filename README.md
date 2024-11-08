# Previsão de Preço de Imóveis - API de Regressão Linear

## Descrição

Este projeto consiste em uma API desenvolvida com Flask, que utiliza um modelo de Regressão Linear treinado para prever o preço de imóveis com base em características como área (sqft), número de quartos, número de banheiros e idade da casa. A API permite que os usuários forneçam essas características em formato JSON e obtenham uma previsão do preço da casa.

## Tecnologias Utilizadas

- ![Flask](https://img.shields.io/badge/Flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white) -> Framework para criação de APIs web.
- ![scikit-learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white) -> Biblioteca para aprendizado de máquina (Machine Learning), utilizada para criar e treinar o modelo de Regressão Linear.
- ![Pandas](https://img.shields.io/badge/Pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white) -> Biblioteca para manipulação e análise de dados.
- ![NumPy](https://img.shields.io/badge/NumPy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white) -> Biblioteca para cálculos numéricos.
- ![joblib](https://img.shields.io/badge/joblib-%23A7A8AA.svg?style=for-the-badge&logo=joblib&logoColor=white) -> Utilizada para salvar e carregar o modelo treinado.

## Funcionalidades

- **Previsão de Preço**: A API permite prever o preço de uma casa com base em quatro parâmetros:
  - Área da casa (sqft_living)
  - Número de quartos
  - Número de banheiros
  - Idade da casa

- **Formatação do Retorno**: O preço previsto é retornado com a formatação monetária em **R$**, com duas casas decimais.

## Como Usar

### Pré-requisitos

- Python 3.x
- Instalar as dependências do projeto

### Instalação

1. Clone este repositório para sua máquina local:
    ```bash
    git clone https://github.com/seu-usuario/nome-do-repositorio.git
    cd nome-do-repositorio
    ```

2. Crie um ambiente virtual (opcional, mas recomendado):
    ```bash
    python -m venv venv
    source venv/bin/activate  # No Windows, use venv\Scripts\activate
    ```

3. Instale as dependências do projeto:
    ```bash
    pip install -r requirements.txt
    ```

### Executando a API

1. Inicie a aplicação Flask:
    ```bash
    python app.py
    ```

2. A API estará disponível no endereço:
    ```
    http://127.0.0.1:5000/
    ```

### Endpoint

#### **POST /prever**

Este endpoint recebe um JSON com os dados da casa e retorna o preço previsto.

Estrutura do Projeto
bash
Copiar código
├── app.py                     # Arquivo principal com a API Flask
├── app/
│   ├── modelo_regressao_linear.pkl  # Modelo treinado em Regressão Linear
│   └── ...                     # Outros arquivos do projeto
├── requirements.txt            # Dependências do projeto
├── README.md                   # Este arquivo
└── ...                         # Outros arquivos

Como Treinar o Modelo:
Execute o script em: notebooks/treinamento_modelo.ipynb para treinar e salvar o modelo.
O modelo será salvo como modelo_regressao_linear.pkl e poderá ser carregado pela API.
Obs.: Caso o modelo seja gerado dentro de /notebooks, mova-o para /app, para que ele
fique no mesmo diretório que a api.
