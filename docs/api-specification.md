### Base URL
http://localhost:8000/api/v1/

## 1. Transactions
# Endpoint
/transactions/              GET     Lista todas as transações
/transactions/{id}/         GET     Detalhes de uma transação
/transactions/{id}/splits/  GET     Lista todos os splits de uma transação

### Exemplos
#### Listar transações
GET /transactions/

# Response 200 OK
[
    {
        "id": 1,
        "amount": "100.00",
        "created_at": "2025-08-29T12:34:56Z",
        "raw_data": {}
    }
]

#### Obter splits de uma transação
GET /transactions/1/splits/

**Response 200 OK**
[
    {
        "id": 1,
        "user": "João",
        "amount": "50.00",
        "status": "pending",
        "raw_data": {}
    },
    {
        "id": 2,
        "user": "Maria",
        "amount": "50.00",
        "status": "pending",
        "raw_data": {}
    }
]

# 2. Splits
## Endpoint	Method	Descrição
/splits/	                    POST	Criar um novo split
/splits/{id}/	                GET	    Detalhes de um split
/splits/{id}/update_status/	    PATCH	Atualizar status do split

## Exemplos
Criar um split

POST /splits/

# Request Body
{
    "transaction": 1,
    "user": "João",
    "amount": "50.00",
    "status": "pending",
    "raw_data": {}
}

# Response 201 Created
{
    "id": 1,
    "transaction": 1,
    "user": "João",
    "amount": "50.00",
    "status": "pending",
    "raw_data": {}
}

## Atualizar status do split
PATCH /splits/1/update_status/

# Request Body
{
    "status": "processed"
}

# Response 200 OK
{
    "id": 1,
    "transaction": 1,
    "user": "João",
    "amount": "50.00",
    "status": "processed",
    "raw_data": {}
}
