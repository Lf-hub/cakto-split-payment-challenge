from django.db import models
from django.utils.text import slugify


class StatusSplit(models.Model):
    name = models.CharField(verbose_name='nome', max_length=65)
    slug = models.SlugField(verbose_name='slug', max_length=65, unique=True, blank=True)

    class Meta:
        verbose_name = 'Situacao do Split'
        verbose_name_plural = 'Situacoes dos Splits'
    
    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Transaction(models.Model):
    amount = models.DecimalField(verbose_name='valor total', max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(verbose_name='data de criacao', auto_now_add=True)
    raw_data = models.JSONField(verbose_name='dados brutos', default=dict)

    class Meta:
        verbose_name = 'Transação'
        verbose_name_plural = 'Transações'
    
    def __str__(self):
        return f"Transaction {self.id} - $ {self.amount}"


class Split(models.Model):
    transaction = models.ForeignKey(
        Transaction,
        verbose_name='transacao',
        related_name="splits",
        on_delete=models.CASCADE
    )
    status = models.ForeignKey(
        StatusSplit,
        verbose_name='Status',
        on_delete=models.PROTECT,
        null=True,
        blank=True
    )
    user = models.CharField(verbose_name='usuario', max_length=100)
    amount = models.DecimalField(verbose_name='valor do split', max_digits=10, decimal_places=2)
    raw_data = models.JSONField(verbose_name='dados brutos', default=dict)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    class Meta:
        verbose_name = 'Split'
        verbose_name_plural = 'Splits'

    def __str__(self):
        return f"{self.user} - R$ {self.amount}"