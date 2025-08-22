class MenuAdmin(admin.ModelAdmin):
   list_display = ('name', 'price', 'available') # Customize fields shown

class OrderAdmin(admin.ModelAdmin):
    list_display = ('customer_name', 'menu_item', 'quantity', 'status')

    admin.site.register(Menu, MenuAdmin)
    admin.site.register(order.OrderAdmin)   
