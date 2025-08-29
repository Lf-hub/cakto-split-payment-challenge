from django.urls import path, include
from rest_framework.routers import DefaultRouter
from payments.views import TransactionViewSet, SplitViewSet


router = DefaultRouter()
router.register(r'transactions', TransactionViewSet, basename='transaction')
router.register(r'splits', SplitViewSet, basename='split')

urlpatterns = router.urls
