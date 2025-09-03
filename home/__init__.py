from django.shortcuts import render

def about_us(request):
    context = {
        'restaurant_name': 'Yummy Restaurant',
        'history': 'Founded in 2005, Yummy Restaurant began as a small family-run café in Tuni. Over the years, it has grown into a beloved local spot known for its fusion cuisine and warm hospitality.',
        'mission': 'To serve delicious, wholesome meals that bring people together and celebrate the rich culinary heritage of Andhra Pradesh.'
    }
    return render(request, 'about_us.html', context)


<!DOCTYPE html>
<html>
<head>
    <title>About Us - {{ restaurant.name }}</title>
</head>
<body>
    <h1>Welcome to {{ restaurant_name }}</h1>
    <h2>Our History</h2>
    <p>{{ history }}</p>
    <h2>Our Mission</h2>
    <p>{{ mission }}</p>
</body>    
</html>    

f

