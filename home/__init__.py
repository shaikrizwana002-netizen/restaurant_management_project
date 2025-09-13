from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()  This ensures only valid email addresses are accepted
    message = forms.CharField(widget=forms.Textarea)

from django.shortcuts import render
forms .forms import ContactForm

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            # You can now use the validated email
        else:
            # Form is invalid, errors will be shown in the template
            pass
    else:
        form = ContactForm()
    
    return render(request, 'contact.html', {'form': form})

<form method="post">
   {% csrf_token %}
   {{ form.as_p }}
   <button type="submit">Send</button>
</form>

{  % if form.errors %}
  <ul>
    { % for field in form %}
       { %for error in field.errors %}
       <li>{{ fields.label }}: {{ error }}</li>
  </ul>    
{ %endif %}