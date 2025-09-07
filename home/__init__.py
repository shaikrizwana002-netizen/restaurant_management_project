# urls.py
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
]

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Login</title>
</head>
<body>
    <h2>Login</h2>
    {% if form.errors %}
        <p style="color: red;">Invalid username or password.</p>
    {% endif %}
    <form method="post">
        {% csrf_token %}
        <label for="id_username">Username:</label>
        <input type="text" name="username" id="id_username" required><br>

        <label for="id_password">Password:</label>
        <input type="password" name="password" id="id_password" required><br>

        <button type="submit">Login</button>
    </form>
</body>
</html>

<form method="post" action="{% url 'login' %}">
    {% csrf_token %}
    <label for="id_username">Username:</label>
    <input type="text" name="username" id="id_username" required>

    <label for="id_password">Password:</label>
    <input type="password" name="password" id="id_password" required>

    <button type="submit">Login</button>
</form>

# settings.py
LOGIN_REDIRECT_URL = '/'