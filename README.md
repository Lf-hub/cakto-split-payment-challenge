# Cakto Split Payment Challenge

Sistema de **Split Payments**, permitindo que criadores digitais dividam automaticamente a receita de vendas com parceiros.

## Stack Tecnológica
- **Backend:** Python 3.11, Django, Django REST Framework
- **Banco de Dados:** PostgreSQL
- **Contêineres:** Docker & Docker Compose
- **Testes:** Django TestCase, DRF APIClient

## Funcionalidades
### Transactions
- `GET /api/v1/transactions/` → lista todas as transações  
- `POST /api/v1/transactions/` → cria uma transação  
- `GET /api/v1/transactions/{id}/` → detalhe da transação  
- `GET /api/v1/transactions/{id}/splits/` → splits de uma transação  

### Splits
- `GET /api/v1/splits/` → lista todos os splits  
- `POST /api/v1/splits/` → cria um split (precisa ter transação existente)  
- `GET /api/v1/splits/{id}/` → detalhe de um split  
- `PATCH /api/v1/splits/{id}/update_status/` → atualiza status do split  

## Instalação e Execução
1. Clone o repositório:
   git clone https://github.com/Lf-hub/cakto-split-payment-challenge.git
   cd cakto-split-payment-challenge/src

2. Crie e ative o ambiente virtual:
   python -m venv .venv
   source .venv/bin/activate

3. Instale dependências:
   pip install -r requirements.txt

4. Configure variáveis de ambiente no .env (exemplo):
   DJANGO_SECRET_KEY=your_secret_key
   DATABASE_URL=postgres://user:password@db:5432/db_name

5. Rode as migrations:
   python manage.py migrate

6. Inicie a aplicação localmente:
   python manage.py runserver

7. Rodar via Docker:
   docker-compose up --build

Testes
1. Rodar todos os testes:
   python manage.py test

2. Rodar uma classe de teste específica:
   python manage.py test payments.tests.APITransactionSplitTest

