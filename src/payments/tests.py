from django.test import TestCase
from django.utils import timezone

from rest_framework import status
from rest_framework.test import APIClient

from payments.models import Transaction, Split, StatusSplit


class TransactionSplitTest(TestCase):
    def setUp(self):
        # criate transaction whit 100
        self.transaction = Transaction.objects.create(
            amount=100.00,
            raw_data={"source": "test"}
        )
        self.status_pending = StatusSplit.objects.create(name="Pendente", slug="pending")

    def test_create_splits(self):
        # splits
        Split.objects.create(transaction=self.transaction, user="João", amount=40.00, status=self.status_pending)
        Split.objects.create(transaction=self.transaction, user="Maria", amount=30.00, status=self.status_pending)
        Split.objects.create(transaction=self.transaction, user="Pedro", amount=30.00, status=self.status_pending)

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


class APITransactionSplitTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.status_pending = StatusSplit.objects.create(name="Pendente", slug="pending")
        self.status_processed = StatusSplit.objects.create(name="Processado", slug="processed")

        self.transaction = Transaction.objects.create(
            amount=100.00,
            raw_data={"info": "teste"},
            created_at=timezone.now()
        )

        self.split = Split.objects.create(
            transaction=self.transaction,
            user="João",
            amount=50.00,
            status=self.status_pending,
            raw_data={"info": "teste split"}
        )

    def test_transaction_list(self):
        response = self.client.get("/api/v1/transactions/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

    def test_transaction_create(self):
        payload = {"amount": 200.0, "raw_data": {"info": "nova"}}
        response = self.client.post("/api/v1/transactions/", payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(float(response.data['amount']), 200.0)

    def test_transaction_detail(self):
        response = self.client.get(f"/api/v1/transactions/{self.transaction.id}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(float(response.data['amount']), 100.0)

    def test_transaction_splits(self):
        response = self.client.get(f"/api/v1/transactions/{self.transaction.id}/splits/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['user'], "João")

    def test_split_list(self):
        response = self.client.get("/api/v1/splits/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

    def test_split_create(self):
        payload = {
            "transaction": self.transaction.id,
            "user": "Maria",
            "amount": 25.0,
            "status": self.status_pending.slug,
            "raw_data": {"info": "split maria"}
        }
        response = self.client.post("/api/v1/splits/", payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['user'], "Maria")

    def test_split_detail(self):
        response = self.client.get(f"/api/v1/splits/{self.split.id}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['user'], "João")

    def test_split_update_status(self):
        payload = {"status": "processed"}
        response = self.client.patch(f"/api/v1/splits/{self.split.id}/update_status/", payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['status'], "processed")