from django.test import TestCase
from .models import Transaction, Split

class TransactionSplitTest(TestCase):
    def setUp(self):
        # criate transaction whit 100
        self.transaction = Transaction.objects.create(
            amount=100.00,
            raw_data={"source": "test"}
        )

    def test_create_splits(self):
        # splits
        Split.objects.create(transaction=self.transaction, user="João", amount=40.00)
        Split.objects.create(transaction=self.transaction, user="Maria", amount=30.00)
        Split.objects.create(transaction=self.transaction, user="Pedro", amount=30.00)

        # getl all transactions
        splits = self.transaction.splits.all()

        # verify has 3 split
        self.assertEqual(splits.count(), 3)

        # verify value
        total_split_amount = sum(s.amount for s in splits)
        self.assertEqual(total_split_amount, self.transaction.amount)

    def test_transaction_str(self):
        self.assertIn("Transaction", str(self.transaction))

    def test_split_str(self):
        split = Split.objects.create(transaction=self.transaction, user="João", amount=50.00)
        self.assertIn("João", str(split))
