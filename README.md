# Data Pipeline Project

Este projeto implementa um pipeline de dados que consome dados de uma API pública e os disponibiliza através de uma API REST.

## Estrutura do Projeto

- `api/`: Contém o código da API Flask.
- `data/`: Contém scripts SQL e dados auxiliares.
- `pipeline/`: Contém o pipeline de dados e utilitários.
- `requirements.txt`: Lista de dependências do projeto.

## Configuração

1. Clone o repositório:
    ```sh
    git clone https://github.com/yourusername/data_pipeline_project.git
    cd data_pipeline_project
    ```

2. Crie e ative um ambiente virtual:
    ```sh
    python -m venv venv
    source venv/bin/activate  # No Windows, use `venv\Scripts\activate`
    ```

3. Instale as dependências:
    ```sh
    pip install -r requirements.txt
    ```

4. Configure o banco de dados:
    ```sh
    python -c "from pipeline import utils; utils.initialize_db()"
    ```

5. Execute o pipeline de dados:
    ```sh
    python -c "from pipeline import data_pipeline; data_pipeline.insert_or_update(2020)"
    ```

6. Inicie a API:
    ```sh
    python api/app.py
    ```

## Endpoints da API

- `GET /area_colhida?municipio_id=<ID>&ano=<ANO>`: Retorna a área colhida para um município e ano específicos.
- `GET /produtividade?estado=<ESTADO>&ano=<ANO>`: Retorna a produtividade de um estado para um ano específico.
- `GET /quantidade_produzida?municipio=<ID>&ano=<ANO>`: Retorna a quantidade produzida para um município e ano específicos.
