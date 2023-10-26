import unittest
import routes
from flask import json

class test(unittest.TestCase):

    def setUp(self):
        self.app = routes.app.test_client()

    def test_top_n(self):
        response = self.app.get('/api/topn?n=5')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        

    def test_invalid_top_n(self):
        response = self.app.get('/api/topn?n=105')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 400)
        self.assertTrue("error" in data)

if __name__ == "__main__":
    unittest.main()
