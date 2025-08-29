from rest_framework import serializers
from .models import Transaction, Split, StatusSplit


class TransactionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Transaction
        fields = ['amount', 'raw_data']


class StatusSplitSerializer(serializers.ModelSerializer):
    class Meta:
        model = StatusSplit
        fields = ['id', 'name', 'slug']


class SplitSerializer(serializers.ModelSerializer):
    status = serializers.SlugRelatedField(
        slug_field='slug',
        queryset=StatusSplit.objects.all()
    )

    class Meta:
        model = Split
        fields = ['id', 'transaction', 'user', 'amount', 'status', 'raw_data']