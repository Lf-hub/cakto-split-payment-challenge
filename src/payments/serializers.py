from rest_framework import serializers
from .models import Transaction, Split


class SplitSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Split
        fields = '__all__'


class TransactionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Transaction
        fields = ['amount', 'raw_data']
        
