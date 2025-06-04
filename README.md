# 📈 API REST - Cotações de Ações da B3

Esta é uma API REST desenvolvida com **FastAPI** que permite consultar cotações de ações da **B3 (Bolsa de Valores do Brasil)**. A API utiliza **PostgreSQL** como banco de dados e conta com **autenticação JWT** para proteger rotas sensíveis.

---

## ✅ Funcionalidades

- 🔐 Autenticação via JWT (login e cadastro de usuários)
- 📊 Consulta de cotações armazenadas no banco de dados
- 🔍 Filtro por ticker e data
- ⚙️ Rotas protegidas para garantir acesso seguro
- 🗃️ Integração com banco de dados PostgreSQL

---

## 📦 Tecnologias Utilizadas

- Python 3.9+
- FastAPI
- PostgreSQL
- SQLAlchemy
- Alembic (migrações)
- Passlib (hash de senhas)
- PyJWT (token JWT)
- Uvicorn (servidor ASGI)

---

## 🚀 Instalação

1. Clone o repositório:

bash
git clone https://github.com/caiodotmm/api-cotacoes-b3.git
cd api-cotacoes-b3

---

## Crie e ative um ambiente virtual:
python -m venv venv
source venv/bin/activate
pip install fastapi uvicorn

---

### Instale as dependências:
pip install -r requirements.txt

---

### Configure o banco de dados PostgreSQL em .env:
DATABASE_URL=postgresql://usuario:senha@localhost:5432/api-cotacoes-b3
SECRET_KEY=sua_chave_secreta
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30

---

### Rode as migrações com Alembic:
alembic upgrade head

--- 

## 📥 Executando a API - localmente

bash
uvicorn app.main:app --reload

---

## 🔐 Autenticação
POST /auth/login
Body:
{
  "username": "usuario1",
  "password": "senha123"
}

Resposta:
{
  "access_token": "seu.jwt.token.aqui",
  "token_type": "bearer"
}

---

## 📌 Obter cotação de uma ação específica
Requisição:
GET /cotacao/{ticker}
Authorization: Bearer {token}

Resposta:
{
  "id": 1,
  "ticker": "PETR4.SA",
  "descricao": "Petrobras S.A"
  "preco": 36.25,
  "data": "2025-06-03"
}

---

## 📌 Obter cotações de múltiplas ações
Requisição:
GET /cotacoes?{tickers}
Authorization: Bearer {token}

Resposta:
[
  {
    "id": 1,
    "ticker": "PETR4.SA",
    "descricao": "Petrobras S.A"
    "preco": 36.25,
    "data": "2025-06-03"
  },
  {
    "id": 1,
    "ticker": "VALE3.SA",
    "descricao": "VALE3 S.A"
    "preco": 36.25,
    "data": "2025-06-03"
  },
  {
    "id": 1,
    "ticker": "ITUB4.SA",
	  "descricao": "ITUB4 S.A"
	  "preco": 36.25,
	  "data": "2025-06-03"
  }
]

---

### 📅 Histórico por data (opcional)
Requisição:
GET /cotacoes/{ticker}?start=2025-01-01&end=2025-06-01
Authorization: Bearer {token}

Resposta:
[
  {
    "id": 1,
    "ticker": "PETR4.SA",
    "descricao": "Petrobras S.A"
    "preco": 36.25,
    "data": "2025-03-01"
  },
  {
    "id": 1,
    "ticker": "PETR4.SA",
    "descricao": "Petrobras S.A"
    "preco": 36.25,
    "data": "2025-02-01"
  },
  {
    "id": 1,
    "ticker": "PETR4.SA",
    "descricao": "Petrobras S.A"
    "preco": 36.25,
    "data": "2025-01-01"
  }
]

---

### 🧪 Como rodar os testes
pytest tests/
pytest --cov=app tests/

---

## ⚙️ Estrutura do Projeto

api-cotacoes-b3/
│
├── app/
│   ├── main.py
│   ├── models/
│   ├── routers/
│   ├── schemas/
│   ├── services/
│   ├── auth/
│   └── database.py
│
├── tests/ 
│
├── alembic/
│   └── versions/
│       ├── env.py
│       ├── README
│       └── script.py.mako
├── .env                   
├── requirements.txt
└── README.md

