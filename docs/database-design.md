# Database Design

Este documento detalha o design do banco de dados para o módulo de **Split Payments**, com foco em auditoria, integridade financeira e performance.

## Histórico e Auditoria

- Todas as transações e splits são registradas com seus **dados brutos** (`raw_data`) para auditoria futura.
- Tabela `StatusSplit` mantém os status de um split, garantindo rastreabilidade das alterações.
- Possibilidade de registrar logs de alterações em futuros eventos (event sourcing ou triggers).

## Integridade Financeira

- **Foreign Keys**:  
  - `Split.transaction` → `Transaction` (CASCADE)
  - `Split.status` → `StatusSplit` (PROTECT)
- **Constraints**:
  - O valor total de splits deve ser igual ao valor da transação (pode ser validado via regras de negócio no Django).
- **Índices**:
  - `Transaction.created_at` → para buscas rápidas por data
  - `Split.transaction` → para consultas de splits de uma transação
  - `Split.status` → para filtrar splits por status

## Performance e Particionamento

- Consultas mais frequentes:
  - `GET /api/v1/transactions/{id}/splits/`
  - `GET /api/v1/splits/?status=pending`
- Para escalar, considerar:
  - **Indices compostos**: `(transaction, status)` para consultas combinadas
