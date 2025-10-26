from django.test import TestCase
from rest_framework.test import APITestCase
from home.models import Restaurant

class RestaurantInfoAPITest(APITestCase):
    def test_get_restaurant_info(self):
        # Step a: Create a sample Restaurant instance
        restaurant = Restaurant.objects.create(
            name='Test Restaurant',
            address='123 Test St'
        )

        # Step b: Make a GET request to the API endpoint
        response = self.client.get('/api/restaurant-info/')

        # Step c: Assert that the response status code is 200
        self.assertEqual(response.status_code, 200)

        # Step d: Assert that the response data matches the sample restaurant
        self.assertEqual(response.data[0]['name'], restaurant.name)
        self.assertEqual(response.data[0]['address'], restaurant.address)
