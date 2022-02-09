import unittest
from app.run import app

class ApiTest(unittest.TestCase):

    def test_timezones_request(self):
        client = app.test_client(self)
        response = client.get('/api/v1/timezones')
        assert response.status_code == 200, "Should return status code 200"

    def test_now_request(self):
        client = app.test_client(self)
        response = client.get('/api/v1/now')
        assert response.status_code == 200, "Should return status code 200"
    
    def test_now_request_with_invalid_timezone(self):
        client = app.test_client(self)
        response = client.get('/api/v1/now?timezone=America/Sao_P')
        assert response.status_code == 400, "Should return status code 400"

if __name__ == '__main__':
    unittest.main()