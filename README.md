# ValidaEstoque

# ValidaEstoque

Sistema de controle de estoque feito em Python. A ideia é facilitar o controle de produtos, principalmente em relação à validade e à quantidade disponível.

> Em desenvolvimento

## Sobre o projeto

O ValidaEstoque foi criado para ajudar no controle de produtos em estoque.

O sistema vai permitir cadastrar produtos, acompanhar suas quantidades e datas de validade e avisar quando algo estiver perto de vencer ou precisar ser comprado novamente.

A ideia também é evitar desperdícios e facilitar o controle do estoque no dia a dia.

## Tecnologias

* Python
* FastAPI
* SQLAlchemy
* SQLite
* Pydantic
* Uvicorn
* Swagger

## Estrutura do projeto

```text
ValidaEstoque/
│
├── database.db
│
└── backend/
    ├── __init__.py
    ├── main.py
    ├── database.py
    ├── models.py
    ├── regras.py
    └── schemas.py
```

### O que cada arquivo faz

**main.py**
É onde fica a API e os endpoints do sistema.

**database.py**
Faz a configuração do banco de dados.

**models.py**
Define como os produtos são armazenados no banco.

**schemas.py**
Define os dados que podem ser enviados para a API e faz a validação deles.

**regras.py**
Contém algumas regras do sistema, como verificar a validade e se o estoque precisa ser reposto.

**database.db**
É o banco de dados SQLite usado pelo projeto.

## O que já foi feito

### CRUD de produtos

A API já permite:

| Método | Endpoint         | O que faz           |
| ------ | ---------------- | ------------------- |
| POST   | `/produtos`      | Cadastra um produto |
| GET    | `/produtos`      | Lista os produtos   |
| GET    | `/produtos/{id}` | Busca um produto    |
| PUT    | `/produtos/{id}` | Atualiza um produto |
| DELETE | `/produtos/{id}` | Exclui um produto   |

### Controle de validade

O projeto já possui uma função que verifica a data de validade do produto.

Ela classifica os produtos em:

```text
vencido
vence_em_breve
seguro
```

A ideia é usar isso posteriormente no dashboard para facilitar a visualização do estoque.

### Estoque mínimo

Também existe uma regra para verificar quando um produto precisa ser comprado novamente.

A lógica atual é:

```text
quantidade <= quantidade_minima
```

Quando isso acontecer, o produto poderá entrar automaticamente na lista de compras.

## Como executar

Primeiro, instale as dependências:

```bash
pip install fastapi uvicorn sqlalchemy pydantic
```

Depois, na pasta principal do projeto, execute:

```bash
python -m uvicorn backend.main:app --reload
```

No Windows, também pode ser necessário usar o caminho completo do Python:

```powershell
& "CAMINHO_DO_PYTHON" -m uvicorn backend.main:app --reload
```

Depois de iniciar o servidor, a API estará disponível em:

```text
http://127.0.0.1:8000/
```

A documentação para testar a API fica em:

```text
http://127.0.0.1:8000/docs
```

## Exemplo de cadastro

Para cadastrar um produto usando `POST /produtos`:

```json
{
  "nome": "Leite",
  "categoria": "Laticínios",
  "quantidade": 10,
  "quantidade_minima": 5,
  "data_validade": "2026-09-10",
  "preco": 5.0
}
```

## Próximos passos

### Sistema

* [x] Criar banco de dados
* [x] Criar modelo de produto
* [x] Criar validação dos dados
* [x] Cadastrar produtos
* [x] Listar produtos
* [x] Buscar produto por ID
* [x] Atualizar produto
* [x] Excluir produto
* [x] Criar regra de validade
* [ ] Mostrar o status de validade na API
* [ ] Criar lista de compras automática
* [ ] Criar relatório de produtos vencidos
* [ ] Calcular dinheiro perdido com produtos vencidos
* [ ] Criar histórico

### Interface

* [ ] Criar dashboard
* [ ] Criar tela de cadastro
* [ ] Criar tabela de produtos
* [ ] Mostrar produtos vencidos
* [ ] Mostrar produtos próximos do vencimento
* [ ] Mostrar produtos com estoque baixo
* [ ] Criar lista de compras
* [ ] Adicionar gráficos

### Futuramente

* [ ] Login de usuários
* [ ] PostgreSQL
* [ ] Notificações por Telegram
* [ ] Notificações por e-mail
* [ ] Leitura de código de barras
* [ ] Consulta de produtos por API
* [ ] Sistema FEFO
* [ ] Deploy

## Ideia principal

O objetivo do projeto é ir além de um simples CRUD.

A ideia é que o sistema consiga analisar o estoque e ajudar a tomar decisões, como:

```text
Produto perto de vencer
        ↓
Identificar automaticamente
        ↓
Priorizar utilização
        ↓
Evitar desperdício
```

E:

```text
Estoque abaixo do mínimo
        ↓
Identificar automaticamente
        ↓
Adicionar à lista de compras
```

## Sobre o projeto

Esse projeto está sendo desenvolvido para praticar programação e aprender, na prática, conceitos como Python, APIs, bancos de dados, backend e organização de projetos.

A ideia é continuar evoluindo o ValidaEstoque até chegar a um sistema completo que possa ser usado como projeto de portfólio.
