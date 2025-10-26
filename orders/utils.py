import logging
from django.core.exceptions import ObjectDoesNotExist
from orders.models import Order  # Adjust this import based on your actual model location
from home.models import MenuItem, get_distinct_cuisine

logger = logging.getLogger(__name__)

def update_order_status(order_id, new_status):
    """
    Updates the status of an order given its ID and the new status.

    Args:
        order_id (int): The ID of the order to update.
        new_status (str): The new status to set.

    Returns:
        bool: True if update was successful, False otherwise.
    """
    try:
        order = Order.objects.get(id=order_id)
        old_status = order.status
        order.status = new_status
        order.save()
        logger.info(f"Order {order_id} status changed from '{old_status}' to '{new_status}'.")
        return True
    except ObjectDoesNotExist:
        logger.error(f"Order with ID {order_id} not found.")
        return False
    except Exception as e:
        logger.exception(f"Unexpected error while updating order {order_id}: {e}")
        return False


def get_distinct_cuisines():
    """
    Returns a list of all unique cuisine names currently used in menu items.
    Useful for building dynamic filters or displaying cuisine options.
    """
    return list(
        MenuItem.objects.values_list('cuisine__name', flat=True).distinct()
    )
