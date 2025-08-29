from django.contrib import admin
from .models import Split, StatusSplit, Transaction


@admin.register(StatusSplit)
class StatusSplitAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug')
    prepopulated_fields = {"slug": ("name",)}
    search_fields = ('name',)


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('id', 'amount', 'created_at')
    search_fields = ('id',)


@admin.register(Split)
class SplitAdmin(admin.ModelAdmin):
    list_display = ('id', 'transaction', 'user', 'amount', 'status')
    list_filter = ('status',)
    search_fields = ('user',)
    autocomplete_fields = ('transaction', 'status')
