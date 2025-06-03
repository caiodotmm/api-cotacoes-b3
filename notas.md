# Notas sobre a B3_Api
## Tarefas inicias
1. Instalar o Docker
	- Criar o Docker
	- PostgreSQL dentro do Docker
	- PgAdmin
2. Criar banco de dados: B3_Cotacao (PostgreSQL)
3. Criar tabelas:
	- Acao(id: primary key, nome: str, descricao: str, status: bool, data_criacao: date, data_atualizacao: date)
	- Cotacoes(id: primary key, id_acao: foreign key, preco: float, data_cotacao: date, data_criacao: date)