from django.core.mail import send_mail, BadHeaderError
from django .conf import settings
import logging

#Set up logging
logger = logging.getLogger(__name__)

def send_order_confirmation_email(order_id, customer_email, customer_name, order_items, total_amount):
  """
  Sends an order confirmation email to the customer.

  Args:
      order_id (str): Unique identifier for the order.
      customer_email (str): Recipient's email address.
      customer_name (str): Name of the customer.
      order_items (list): List of items in the order.
      total_amount (float): Total cost of the order.

   Returns:
      dict: Result status and and message.
   """
   subject = f"Order Confirmation _ #{order_id}"
   item_list = "\n".join([f"-{items}" for item in order_items])
   message = (
    f"Dear {customer_name},\n\n"
    f"Thankn you for your order!\n\n"
    f"Order ID: {order_id}\n"
    f"Items:\n{item_list}\n\n"
    f"Total Amount: ₹{total_amount:.2f}\n\n"
    f"Best regards,\nYour Company Name"
   )
   from_email = settings.DEAFAULT_FROM_EMAIL

   try:
      send_mail(subject, message,from_email, [customer_email])
      return {"status": "success", "message": "Confirmation email sent success."}
      except BadHeaderError:
        logger.error(f"Bad header error while sending email to {customer_email})
        return {"status": "error", "message": "Invalid header found."}
      except Exception as e:
        logger.error(f"Error sending email to {customer_email}: {e}")
        return {"status": "error", "message": "Failed to send confirmation email."}  


EMAIL_BACKEND = 'django.core.mail.backend.smtp.EmailBackend'
EMAIL_HOST = 'smtp.yourprovider.com'
EMAIL_PORT  = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your_email@example.com'
EMAIL_HOST_PASSWORD = 'your_password'
DEFAULT_FROM_EMAIL = 'Your Company <your_email@example.com>'       