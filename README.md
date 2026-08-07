# FastAPI Zero

Projeto desenvolvido para estudo e prática com **FastAPI**, utilizando **Poetry** para gerenciamento de dependências e **Taskipy** para automação de tarefas.

## Tecnologias

- Python 3.13+
- FastAPI
- Poetry
- Ruff
- Pytest
- Taskipy

## Pré-requisitos

Antes de começar, instale:

- Python 3.13 ou superior
- Poetry

Verifique se ambos estão instalados:

```bash
python --version
poetry --version
```

## Clonando o projeto

```bash
git clone https://github.com/SEU-USUARIO/fastapi-zero.git
cd fastapi-zero
```

## Instalando as dependências

Instale todas as dependências do projeto:

```bash
poetry install
```

## Ativando o ambiente virtual

Caso queira entrar no ambiente virtual:

```bash
poetry shell
```

Ou execute qualquer comando utilizando:

```bash
poetry run
```

## Executando o projeto

Inicie o servidor de desenvolvimento:

```bash
task run
```

ou

```bash
poetry run task run
```

A aplicação ficará disponível em:

- http://127.0.0.1:8000

Documentação da API:

- Swagger: http://127.0.0.1:8000/docs
- ReDoc: http://127.0.0.1:8000/redoc

## Comandos úteis

### Executar o lint

```bash
task lint
```

### Corrigir automaticamente problemas encontrados

```bash
task pre_format
```

### Formatar o código

```bash
task format
```

### Executar os testes

```bash
task test
```

Após a execução dos testes, será gerado um relatório de cobertura em:

```text
htmlcov/
```

## Estrutura do projeto

```text
fastapi-zero/
├── fastapi_zero/
│   ├── app.py
│   └── ...
├── tests/
├── pyproject.toml
├── poetry.lock
└── README.md
```

## Dependências

### Produção

- FastAPI

### Desenvolvimento

- Ruff
- Pytest
- pytest-cov
- Taskipy

## Licença

Projeto desenvolvido para fins de estudo.