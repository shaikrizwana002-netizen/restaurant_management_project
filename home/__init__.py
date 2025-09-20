# utils/validation_utils.py

from email_validator import validate_email, EmailNotValidError
import logging

logger = logging.getLogger(__name__)

def is_valid_email(email: str) -> bool:
    try:
        # Validate and normalize the email
        validate_email(email)
        return True
    except EmailNotValidError as e:
        # Log the error for debugging
        logger.warning(f"Invalid email '{email}': {e}")
        return False
# views.py

from utils.validation_utils import is_valid_email

ef submit_email(request):
    email = request.POST.get('email')
    if is_valid_email(email):
        # Proceed with saving or processing
        ...
    else:
        # Return error response
        ...