# ValidaEstoque

Sistema de gerenciamento e controle de estoque desenvolvido com **Python**, **FastAPI**, **SQLAlchemy** e **SQLite**.

O ValidaEstoque permite cadastrar produtos, acompanhar seus níveis de estoque, verificar datas de validade e gerar relatórios para auxiliar no controle e na tomada de decisões.

## Funcionalidades

* Cadastro de produtos
* Listagem de produtos
* Consulta individual de produtos
* Edição de produtos
* Exclusão de produtos
* Controle de quantidade mínima em estoque
* Identificação de produtos com estoque baixo
* Verificação automática da validade dos produtos
* Identificação de produtos vencidos
* Identificação de produtos próximos do vencimento
* Cálculo do valor total do estoque
* Cálculo de possíveis prejuízos com produtos vencidos
* Geração de lista de compras
* Dashboard com indicadores do estoque

## Tecnologias utilizadas

* **Python 3.14+**
* **FastAPI** — criação da API e do backend
* **SQLAlchemy** — comunicação com o banco de dados
* **SQLite** — banco de dados
* **HTML5**
* **CSS3**
* **JavaScript**
* **Uvicorn** — servidor da aplicação

## Estrutura do projeto

```text
ValidaEstoque/
│
├── backend/
│   ├── __init__.py
│   ├── database.py
│   ├── index.html
│   ├── main.py
│   ├── models.py
│   ├── regras.py
│   ├── schemas.py
│   │
│   └── templates/
│       └── index.html
│
├── validaestoque/
│
├── database.db
│
└── README.md
```

> Dependendo da configuração utilizada, o `index.html` pode estar diretamente dentro de `backend` ou na pasta `backend/templates`.

## Principais arquivos

### `main.py`

Arquivo principal da aplicação.

Responsável por:

* Inicializar o FastAPI
* Criar as tabelas do banco
* Disponibilizar as rotas da API
* Realizar as operações de CRUD
* Gerar relatórios
* Disponibilizar o dashboard

### `database.py`

Responsável pela configuração da conexão com o banco de dados SQLite e pela criação da base SQLAlchemy.

### `models.py`

Define os modelos utilizados no banco de dados, incluindo o modelo de produto.

### `schemas.py`

Define os schemas utilizados para validação dos dados recebidos pela API.

### `regras.py`

Contém as regras de negócio do sistema, como:

* Verificação da validade
* Identificação de produtos próximos do vencimento
* Verificação de estoque abaixo do mínimo

### `index.html`

Interface visual do sistema, permitindo ao usuário visualizar e administrar os produtos.

## API

O sistema possui as seguintes principais rotas:

| Método   | Rota                       | Função                                       |
| -------- | -------------------------- | -------------------------------------------- |
| `GET`    | `/`                        | Abre a interface do sistema                  |
| `POST`   | `/produtos`                | Cadastra um produto                          |
| `GET`    | `/produtos`                | Lista todos os produtos                      |
| `GET`    | `/produtos/{id}`           | Consulta um produto                          |
| `PUT`    | `/produtos/{id}`           | Atualiza um produto                          |
| `DELETE` | `/produtos/{id}`           | Exclui um produto                            |
| `GET`    | `/lista-compras`           | Lista produtos que precisam ser comprados    |
| `GET`    | `/relatorio/vencidos`      | Relatório de produtos vencidos               |
| `GET`    | `/relatorio/vencendo`      | Relatório de produtos próximos do vencimento |
| `GET`    | `/relatorio/estoque-baixo` | Relatório de estoque baixo                   |
| `GET`    | `/dashboard`               | Indicadores gerais do estoque                |
| `GET`    | `/resumo`                  | Resumo geral do estoque                      |

## Dados dos produtos

Cada produto possui informações como:

* Nome
* Categoria
* Quantidade atual
* Quantidade mínima
* Data de validade
* Preço

O sistema utiliza essas informações para realizar automaticamente os cálculos e classificações.

## Regras de estoque

Um produto é considerado com **estoque baixo** quando sua quantidade atual é menor ou igual à quantidade mínima configurada.

Quando isso acontece, o sistema calcula automaticamente a quantidade necessária para atingir novamente o estoque mínimo.

```text
Quantidade a comprar =
Quantidade mínima - Quantidade atual
```

## Regras de validade

O sistema verifica automaticamente a data de validade de cada produto.

Os produtos podem ser classificados como:

* **Vencido**
* **Vence em breve**
* **Seguro**

Essa classificação é utilizada no dashboard e nos relatórios.

## Dashboard

O dashboard apresenta informações gerais do estoque, incluindo:

* Total de produtos
* Produtos vencidos
* Produtos próximos do vencimento
* Produtos seguros
* Produtos com estoque baixo
* Prejuízo estimado com produtos vencidos

## Como executar o projeto

### 1. Clonar ou baixar o projeto

Baixe o projeto e abra o terminal na pasta principal:

```powershell
cd C:\Users\Nogueira\Downloads\ValidaEstoque
```

### 2. Instalar as dependências

Execute:

```powershell
pip install fastapi uvicorn sqlalchemy
```

### 3. Iniciar o servidor

Execute:

```powershell
python -m uvicorn backend.main:app --reload
```

Se estiver tudo correto, o servidor ficará disponível em:

```text
http://127.0.0.1:8000
```

### 4. Acessar o sistema

Abra no navegador:

```text
http://127.0.0.1:8000
```

## Documentação da API

O FastAPI disponibiliza automaticamente uma documentação interativa.

### Swagger UI

Acesse:

```text
http://127.0.0.1:8000/docs
```

### ReDoc

Também é possível utilizar:

```text
http://127.0.0.1:8000/redoc
```

Essas páginas permitem visualizar e testar as rotas da API diretamente pelo navegador.

## Banco de dados

O projeto utiliza **SQLite**, com o arquivo:

```text
database.db
```

As tabelas são criadas automaticamente pelo SQLAlchemy quando a aplicação é iniciada.

## CRUD

O sistema implementa as quatro operações básicas de gerenciamento:

**Create**

Cadastro de novos produtos.

**Read**

Consulta e listagem dos produtos.

**Update**

Atualização dos dados de produtos existentes.

**Delete**

Exclusão de produtos.

## Objetivo do projeto

O ValidaEstoque foi desenvolvido com o objetivo de criar uma solução simples para gerenciamento de estoque, automatizando tarefas como acompanhamento de quantidades, controle de validade, identificação de produtos que precisam ser repostos e geração de indicadores.

O projeto também demonstra a utilização prática de uma arquitetura baseada em **API REST**, banco de dados e interface web.

## Status do projeto
## Autor

**Enzo Nogueira**

Projeto desenvolvido para fins de aprendizado e aplicação prática de desenvolvimento de software.
