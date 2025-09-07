<!__ templates/base.html __>
<body>
     {% block breadcrumbs %}
     <! __Breadcrumbs will be injected here __>
     {% endblock %}

     {% block content %}
     <!__Page_specific content __>
     {% endblock %}
</body>

{% extends 'base.html' %}

{% block breadcrumbs %}
<nav aria-label="breadcrumb">
   <ol>
     <li><a href="{% url 'home" %} ">Home</a></li>
   </ol>
</nav>{% endblock content %}
<h1>Welcome to Our Site</h1>
{% endblock %}


{% extends 'base.html' %}

{% block breadcrumbs %}
<nav aria-label="breadcrumb">
   <ol>
     <li>a href="{% url 'home' %}">Home</a></li>
     <li>Menu</li>
   </ol>  
</nav>
{% endblock %}

{% block content %}
<h1>Our Menu</h1>
{% endblock %}

{% extends 'base.html' %}

{% block breadcrumbs %}
<nav aria-label="breadcrumb">
  <ol>
    <li><a href="{% url 'home' %} <li><a href="{% url 'home' %}">Home</a></li>
    <li><a href="{% url 'menu' %}">Menu</a></li>
    <li>Order Confirmation</li>
  </ol>
</nav>
{% endblock %}

{% block content %}
<h1>Thank You for Your Order!</h1>
{% endblock %}

