from django.db import models

class ContactForms(models.Model):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)
    
from django.core.mail import send_mail
from django.shortcuts import render,redirect
from .forms import ContactForm

def contact_view(request):
       form = ContactForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        send_mail(
            subject=f"Message from {form.cleaned_data['name']}",
            message=form.cleaned_data['message'],
            from_email=form.cleaned_data['email'],
            recipient_list=['yourrestaurant@example.com']
        )
        return render(request, 'success.html')
    return render(request, 'contact.html', {'form': form})

<!__ contact.html __>
<form method="POST">
    {% csrf_token %>}
    {{ form.as_p }}    
    <button type="submit">Send</button>
</form>

<!__ success.html __>
<p>Thanks! Your message was sent.</p>

EMAIL_BACKEND = 'django.core.mail.backend.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'yourrestaurant@example.com'
EMAIL_HOST_PASSWORD = 'yourpassword'