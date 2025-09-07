# home/__init__.py
# should be empty or contain package-level Python code only
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Privacy Policy</title>
</head>
<body>
     <h1>Privacy Policy</h1>
     <p>
        We value your privacy and are committed to protecting your personal information. This Privacy Policy outlines how we collect, use, and safeguard your data
     </p>
     <h2>Information Collection</h2>
     <p>
       We may collect personal information such as your name, email address, and usage data to improve our services.
     </p>   
</body>
</html>


# views.py
from django.shortcuts import render

def privacy_policy(request):
    return render(request, 'privacy_policy.html')

<!__ home.html __>
<footer>
      <a href="{% url 'privacy_policy' %}">Privacy Policy</a>
</footer>