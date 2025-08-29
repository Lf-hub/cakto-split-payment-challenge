from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from payments.models import Transaction, Split, StatusSplit
from payments.serializers import TransactionSerializer, SplitSerializer

class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

    @action(detail=True, methods=['get'])
    def splits(self, request, pk=None):
        transaction = self.get_object()
        serializer = SplitSerializer(transaction.splits.all(), many=True)
        return Response(serializer.data)


class SplitViewSet(viewsets.ModelViewSet):
    queryset = Split.objects.all()
    serializer_class = SplitSerializer

    @action(detail=True, methods=['patch'])
    def update_status(self, request, pk=None):
        split = self.get_object()
        status_slug = request.data.get('status')

        try:
            status_obj = StatusSplit.objects.get(slug=status_slug)
        except StatusSplit.DoesNotExist:
            return Response(
                {"error": "Status inválido"},
                status=status.HTTP_400_BAD_REQUEST
            )

        split.status = status_obj
        split.save()
        serializer = SplitSerializer(split)
        return Response(serializer.data)