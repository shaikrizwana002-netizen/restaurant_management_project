settings.py
RESTAURANT_PHONE = "+91_98709868977"


(views.py)
from django.conf import settings
def home_view(request):
    phone = settings.RESTAURANT_PHONE
    return render(request, 'index.html', {'phone':phone})

(index.html)    
<p> call us: {{ phone}}</p>
