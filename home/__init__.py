from django.core.mail import send_mail, BadHeaderError
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.conf import settings
import logging

logger = logging.getLogger(__name__)

def send_custom_email(recipient_email, subject, message_body):
    """
    Sends an email using Django's email backend.

    Args:
        recipient_email (str): Recipient's email address.
        subject (str): Subject of the email.
        message_body (str): Body of the email.

    Returns:
        bool: True if email sent successfully, False otherwise.
    """
    try:
        validate_email(recipient_email)
        send_mail(
            subject,
            message_body,
            settings.DEFAULT_FROM_EMAIL,
            [recipient_email],
            fail_silently=False,
        )
        return True
        except ValidationError:
        logger.error(f"Invalid email address: {recipient_email}")
    except BadHeaderError:
        logger.error("Bad header found in email.")
    except Exception as e:
        logger.error(f"Failed to send email: {str(e)}")
    
    return False
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .utils import send_custom_email

class ContactEmailView(APIView):
    def post(self, request):
        email = request.data.get("email")
        subject = request.data.get("subject")
        message = request.data.get("message")

        if send_custom_email(email, subject, message):
            return Response({"message": "Email sent successfully."}, status=status.HTTP_200_OK)
        return Response({"error": "Failed to send email."}, status=status.HTTP_400_BAD_REQUEST)

        