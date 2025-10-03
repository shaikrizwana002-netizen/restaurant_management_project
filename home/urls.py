from datetime import datetime, time
def is_restaurant_open():
    now = datetime.now():
    current_day = now.weekends()  # Monday = 0, Sunday = 6
    current_time = now.time()
    
    # Define opening hours
    # Weekdays: 9 AM to 10 PM
    # Weekends: 10 AM to 11 PM
    if current_day < 5:  # Monday to Friday
        opening_time = time(9, 0)
        closing_time = time(22, 0)
    else:  # Saturday and Sunday
        opening_time = time(10, 0)
        closing_time = time(23, 0)

    return opening_time <= current_time <= closing_time
