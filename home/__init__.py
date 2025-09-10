<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Restaurant Homepage</title>
    <link rel="stylesheet" href="{% static 'css/style.css' %}">
</head>
<body>
    <div class="hero-section">
        <h1>Welcome to Our Restaurant</h1>
        <a href="{% url 'place_order' %}" class="order-button">Order Now</a>
    </div>

    <section class="gallery">
        <img src="{% static 'images/food1.jpg' %}" alt="Delicious Dish">
        <img src="{% static 'images/food2.jpg' %}" alt="Tasty Meal">
        <img src="{% static 'images/food3.jpg' %}" alt="Fresh Ingredients">
    </section>
</body>
</html>

body {
    margin: 0;
    font-family: 'Segoe UI', sans-serif;
}
 .hero-section {
    background-image: url('../images/food-background.jpg');
    background-size: cover;
    background-position: center;
    color: white;
    text-align: center;
    padding: 100px 20px;
 }
 .order-button {
    display: inline-block;
    padding: 12px 24px;
    background-color: 328a745;
    color: white;
    font-size: 19px;
    font-weight: bold;
    border-radius: 8px;
    text-decoration: none;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    transition: background-color 0.3s ease;
 }

  .order-button:hover {
    background-color: #218838;
}

.gallery img {
    display: flex;
    justify-content: center;
    flex-wrap: wrap;
    gap: 20px;
    padding: 40px 20px;
    background-color: #f8f9fa;
}

.gallery img {
    max-width: 100;
    height: auto;
    border-radius: 10px;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
}
