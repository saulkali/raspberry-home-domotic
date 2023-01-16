from fastapi.testclient import TestClient
from app import run

import unittest

class LoginTest(unittest.TestCase):
    def setUp(self) -> None:
        self.client = TestClient(run.app)

    def test_get_login(self):
        response = self.client.get("/login")
        self.assertEqual(response.status_code,200)