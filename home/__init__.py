from django.db import models

class ContactForms(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.CharField(widget=forms.Textarea)
    
<! __home.html __>
<form method="get">
  <input type="text" name="q" " placeholder="Search menu..." value="{{ query }}">
  <button type="submit"Search</button>
</form>

<ul>
  {% for item in items %}
    <li><strong>{{ item.name }}</strong>: {{ item.description }}</li>
  {% empty %}
    <li>No items found.</li>
  {% endfor %}
</ul>

