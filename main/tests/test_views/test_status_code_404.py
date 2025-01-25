
from rest_framework import status

def test_nonexistent_endpoint(self):
    response = self.client.get('/api/nonexistent-endpoint/')
    self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
