# Plano de Execução – Split Payments

Este plano detalha a implementação do módulo **Split Payments**, organizado em Sprints e fases de go-live.

## Sprint 1-2: Foundation

- Criar models básicos: `Transaction`, `Split`, `StatusSplit`
- Configurar serializers e viewsets iniciais
- Configurar Docker, banco Postgres e ambiente local
- Implementar testes unitários iniciais
- Garantir que endpoints de leitura (`GET`) estão funcionando

## Sprint 3-4: Core Implementation

- Implementar criação de splits (`POST /splits/`)
- Implementar atualização de status (`PATCH /splits/{id}/update_status/`)
- Criar validações de negócio:
  - Valor total de splits = valor da transação
  - Limite de usuários por transação (regras futuras)
- Implementar testes de integração da API
- Documentar endpoints com exemplos de request/response
- Preparar métricas iniciais de observabilidade (latência, status, falhas)

## Sprint 5-6: Production Readiness

- Testes de carga e performance
- Configurar alertas críticos e monitoramento
- Criar scripts de migração e dados iniciais (`StatusSplit`)
- Documentar plano de rollback:
  - Reversão de migrações
  - Desativação de endpoints temporariamente
- Critérios de Go-Live:
  - Todos os testes unitários e de integração passados
  - Métricas de monitoramento ativas
  - Docker e ambiente de produção configurados

## Observações
- Backward compatibility: alterações no banco de dados devem ser compatíveis com transações existentes
- Monitoramento contínuo de splits e transações
- Possibilidade de feature flags para ativar/desativar a funcionalidade
