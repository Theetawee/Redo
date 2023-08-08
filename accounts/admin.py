from django.contrib import admin
from .models import Account

class AccountAdmin(admin.ModelAdmin):
    # Fields to be displayed in the list view of the admin interface
    list_display = ('id', 'username', 'email', 'is_active', 'date_joined')
    
    # Fields that can be used for filtering the accounts in the admin interface
    list_filter = ('is_active', 'date_joined')
    
    # Fields that can be searched in the admin interface
    search_fields = ('username', 'email')

    # Customize the display of the individual account's detail page
    # You can use 'fields' or 'fieldsets' to customize the layout.
    # Example using 'fields':
    # fields = ('username', 'email', 'is_active', 'date_joined')
    
    # Example using 'fieldsets':
    fieldsets = (
        ('Basic Information', {
            'fields': ('first_name','last_name','username', 'email','phone')
        }),
        ('Status', {
            'fields': ('is_active', 'date_joined','status','verified_email')
        }),
    )

# Register the Account model with the custom admin class
admin.site.register(Account, AccountAdmin)
