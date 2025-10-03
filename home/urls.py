from datetime import date
from django.db.models import Sum
from .models import Order

def get_daily_sales_total(target_date):
   order = Orders.objects.filter(created_At_date=target_date)
   total = orders.aggregate(total_sum=Sum('total_price'))['total_sum']
   return total or 0   