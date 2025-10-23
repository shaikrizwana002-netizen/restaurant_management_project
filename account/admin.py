from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Restaurant

class RestaurantAdmin(admin.ModelAdmin):
    # Fields to display in the list view
    list_display = ('name', 'address', 'phone_number', 'email')

    # Fields to enable search functionality
    search_fields = ('name', 'address')

    # Optional: Add filter if is_active exists
    list_filter = ('is_active',) if hasattr(Restaurant, 'is_active') else ()
