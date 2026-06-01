
# Projeto MLOps - Previsão de Preço de Diamantes

![Python](https://img.shields.io/badge/Python-3.13-blue?logo=python)  
![MLflow](https://img.shields.io/badge/MLflow-Tracking-00AEEF)  
![Pytest](https://img.shields.io/badge/Pytest-Testing-green)  
![MLOps](https://img.shields.io/badge/MLOps-Laboratory-orange)

Projeto desenvolvido durante a disciplina **MLOps - Running ML in Production Environments** da Faculdade Impacta.

O objetivo deste projeto é demonstrar a evolução de um experimento de Machine Learning realizado em notebook para uma solução organizada, reproduzível e preparada para automação.

----------

# Evolução do Projeto

## Aula 01

Implementação inicial do fluxo de Machine Learning:

-   EDA
    
-   Feature Engineering
    
-   Treinamento
    
-   Avaliação
    
-   Registro de experimentos com MLflow
    

Resultado:

```text
Notebook + MLflow

```

----------

## Aula 02

Organização do projeto:

-   Estruturação de diretórios
    
-   Separação da lógica de dados
    
-   Criação de módulos Python
    
-   Controle de dependências
    
-   Primeiro teste automatizado com Pytest
    

Resultado:

```text
Projeto organizado e reutilizável

```

----------

## Próximas Etapas

### Aula 03

-   Pipeline de treinamento
    
-   GitHub Actions
    
-   Testes automatizados
    

### Aula 04

-   Deploy
    
-   Monitoramento
    
-   Encerramento do projeto
    

----------

# Arquitetura Atual

```text
                 ┌─────────────┐
                 │  Notebook   │
                 └──────┬──────┘
                        │
                        ▼
                 ┌─────────────┐
                 │ src/data.py │
                 └──────┬──────┘
                        │
                        ▼
                 ┌─────────────┐
                 │ Train/Test  │
                 └──────┬──────┘
                        │
                        ▼
                 ┌─────────────┐
                 │   MLflow    │
                 └──────┬──────┘
                        │
                        ▼
                 ┌─────────────┐
                 │ Experiments │
                 └─────────────┘

```

----------

# Estrutura Atual

```text
impacta-mlops/

├── notebooks/
│   ├── EDA_diamond.ipynb
│   ├── 01_train.ipynb
│   └── 02_train.ipynb
│
├── src/
│   ├── __init__.py
│   └── data.py
│
├── tests/
│   └── test_data.py
│
├── app/
│
├── mlruns/
│
├── requirements.txt
├── README.md
├── pytest.ini
└── .gitignore

```

----------

# Módulo de Dados

O arquivo:

```text
src/data.py

```

centraliza toda a lógica relacionada aos dados.

Funções disponíveis:

```python
load_diamonds()

split_features_target()

train_test_split_diamonds()

```

Benefícios:

-   Reutilização
    
-   Padronização
    
-   Menos código nos notebooks
    
-   Maior reprodutibilidade
    

----------

# Testes Automatizados

O projeto possui seu primeiro teste automatizado.

Arquivo:

```text
tests/test_data.py

```

Executar:

```bash
pytest

```

Resultado esperado:

```text
1 passed

```

----------

# MLflow

Os experimentos continuam sendo registrados utilizando MLflow.

Executar interface:

```bash
mlflow ui

```

Acessar:

```text
http://localhost:5000

```

Através da interface é possível:

-   Comparar execuções
    
-   Visualizar métricas
    
-   Analisar parâmetros
    
-   Consultar artefatos gerados
    

----------

# Instalação

Criar ambiente virtual:

```bash
python -m venv .venv

```

Ativar:

```bash
.\.venv\Scripts\activate

```

Instalar dependências:

```bash
pip install uv

uv pip install -r requirements.txt

```

----------

# Conceitos Trabalhados

-   EDA
    
-   Feature Engineering
    
-   Reprodutibilidade
    
-   Versionamento
    
-   Organização de Projetos
    
-   MLflow
    
-   Pytest
    
-   MLOps
    

----------

# Próximo Passo

Na Aula 03 iremos automatizar o treinamento e integrar o projeto ao GitHub Actions, criando o primeiro pipeline automatizado do projeto.