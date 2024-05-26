from django.contrib import admin
from .models import Account, Destination

@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ('email', 'account_id', 'account_name', 'website')
    search_fields = ('email', 'account_name')
    readonly_fields = ('account_id', 'app_secret_token')

@admin.register(Destination)
class DestinationAdmin(admin.ModelAdmin):
    list_display = ('account', 'url', 'http_method')
    search_fields = ('account__email', 'url')
    list_filter = ('http_method',)