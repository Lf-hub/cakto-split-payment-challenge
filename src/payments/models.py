from django.db import models


class Transaction(models.Model):
    amount = models.DecimalField(verbose_name='Valor total', max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(verbose_name='Data de criação', auto_now_add=True)
    raw_data = models.JSONField(verbose_name='Dados brutos', default=dict)

    class Meta:
        verbose_name = 'Transação'
        verbose_name_plural = 'Transações'
    
    def __str__(self):
        return f"Transaction {self.id} - $ {self.amount}"


class Split(models.Model):
    transaction = models.ForeignKey(
        Transaction,
        verbose_name='Transação',
        related_name="splits",
        on_delete=models.CASCADE
    )
    user = models.CharField(verbose_name='Usuário', max_length=100)
    amount = models.DecimalField(verbose_name='Valor do split', max_digits=10, decimal_places=2)
    raw_data = models.JSONField(verbose_name='Dados brutos', default=dict)

    class Meta:
        verbose_name = 'Split'
        verbose_name_plural = 'Splits'

    def __str__(self):
        return f"{self.user} - R$ {self.amount}"