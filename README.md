# Projeto Churn

Projeto desenvolvido na disciplina de Redes Neurais, com o objetivo de prever o abandono de clientes (churn) utilizando diversos modelos de aprendizado de máquina, incluindo técnicas clássicas e arquiteturas modernas baseadas em atenção.

## 📌 Objetivo

Construir e comparar modelos de classificação para prever a probabilidade de um cliente abandonar um serviço, utilizando diferentes abordagens de machine learning e deep learning. Dataset: https://www.kaggle.com/datasets/kapturovalexander/customers-churned-in-telecom-services

## 🧠 Modelos Utilizados

- **Random Forest (RF)**
- **Gradient Boosting**
- **Multi-Layer Perceptron (MLP)**
- **KAN (Kolmogorov-Arnold Networks)**
- **TabKAN** : https://github.com/kailanefelix/tabkanet-redes-neurais 
- **Stochastic Transformer**
- **STAB** : https://github.com/kailanefelix/stab-redes-neurais

## 📁 Estrutura do Projeto

- `notebooks/`: Contém os notebooks Jupyter com o desenvolvimento dos modelos e análises.
- `environment.yml`: Arquivo para criação do ambiente Conda com todas as dependências necessárias.

## ⚙️ Requisitos

- Python 3.8+
- Conda (recomendado)

Para instalar as dependências, execute:

```bash
conda env create -f environment.yml
conda activate projeto-churn
```

## 📊 Métricas de Avaliação

Os modelos foram avaliados utilizando as seguintes métricas:

- Acurácia
- F1-Score
- AUC-ROC
- KS

## 📈 Resultados

Os resultados obtidos por cada modelo estão detalhados nos notebooks correspondentes, permitindo uma comparação clara do desempenho entre as diferentes abordagens.
