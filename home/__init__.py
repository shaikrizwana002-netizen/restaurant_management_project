class AboutUs(models.Model):
    description = models.TextField()
    image = models.ImageField(upload_to='about_us/')

def about_us_display(request):
    about_us = AboutUs.objects.last()
    return render(request, 'about_us_display.html', {'about_us': about_us})

<div class="about_us_section">
   {% if about_us.image %}
     <img src"{{ anbout_us.image.url }}" alt="Fusion Restaurant" style="max-width: 100%; border_radius: 8px;">
     {% endif %}
     <p>{{ about_us.description }}</p>
</div>     