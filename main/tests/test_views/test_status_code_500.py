

def test_server_error(self):
    with self.assertRaises(Exception):
        response = self.client.get('/api/some-endpoint-that-raises-error/')
