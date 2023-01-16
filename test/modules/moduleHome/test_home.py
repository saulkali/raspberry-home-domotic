from fastapi.testclient import TestClient
import unittest
from app import run
class HomeTest(unittest.TestCase):
    def setUp(self) -> None:
        self.client = TestClient(run.app)

    def test_get_home(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code,200)