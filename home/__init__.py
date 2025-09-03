from django import forms
 
class ContactForm(forms.Form):
    email = forms.EmailField(
        request=True,
        widget=forms.EmailInput(attrs={'placeholder': 'Your email'})
    )
    message = forms.CharField(
        required=True,
        widget=forms.Textarea(attrs={'placeholder': 'Your email'})
        min_length=10
    ) 