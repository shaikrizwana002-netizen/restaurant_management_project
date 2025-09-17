touch orders/utils.py

# orders/utils.py
import string
import secrets
from orders.models import Coupon # Adjust this import based on your actual mode name

def generate_coupon_code(length=10):
    characters = string.ascii_uppercase + string.digits
    while True:
     code = ''.join(secrets.choice(characters) for _ in  range(length))
     if not Coupon.objects.filter(code=code).exists():
        return code  # ← This must be inside the 'if' block

from orders.utils import generate_coupon_code
new_code = generate_coupon_code()
coupon = Coupon.objects.create(code=new_code, discount=20)