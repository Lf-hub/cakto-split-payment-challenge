1. Microsserviço, módulo monolítico ou arquitetura híbrida?

Híbrida: partes críticas em microsserviços e o resto em monolito para simplicidade.

2. Como garantir consistência e atomicidade nos splits?

Cada operação de pagamento deve acontecer inteira ou não acontecer, usando transações do banco ou filas que processam uma por vez.

3. Event sourcing vale a pena para auditoria financeira?

É uma boa prática, ajuda a ter um histórico completo de tudo que aconteceu.

4. Estratégia de deploy sem downtime?

Fazer deploy alternando entre versões e garantir que o banco continue funcionando com a versão antiga.

5. Que métricas de monitoramento são críticas?

Tempo de resposta e falhas nas transações, consumo de CPU e memória, tamanho das filas e avisos se houver erro nos cálculos financeiros.