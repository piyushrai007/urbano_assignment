# Authentication/tests.py
def test_register_user(self):
    url = reverse('signup')
    data = {
        "username": "testuser",
        "password": "password123",
        "email": "testuser@example.com"
    }
    response = self.client.post(url, data, format='json')
    print(response.data)  # Print response to see the error message
    self.assertEqual(response.status_code, status.HTTP_201_CREATED)
