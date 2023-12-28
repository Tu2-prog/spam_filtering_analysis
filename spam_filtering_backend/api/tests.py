import json
import os
from unittest.mock import patch
from django.test import TestCase
from django.urls import reverse
from api.classifier import NaiveBayesClassifier


class APIViewsTestCase(TestCase):
    def setUp(self):
        os.environ["AUTH_TOKEN"] = "test_token"

    def test_authenticate_view(self):
        url = reverse("authenticate")
        valid_token = "test_token"
        invalid_token = "invalid_token"
        invalid_json = "invalid_json"

        # Test with a valid token
        response = self.client.post(
            url, json.dumps({"token": valid_token}), content_type="application/json"
        )
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.json()["validated"])

        # Test with an invalid token
        response = self.client.post(
            url, json.dumps({"token": invalid_token}), content_type="application/json"
        )
        self.assertEqual(response.status_code, 200)
        self.assertFalse(response.json()["validated"])

        # Test with Decode error
        response = self.client.post(url, invalid_json, content_type="application/json")
        self.assertEqual(response.status_code, 400)

        # Test with invalid request method
        response = self.client.get(url)
        self.assertEqual(response.status_code, 405)

    @patch("api.views.joblib.load")
    def test_classify_view(self, mock_joblib_load):
        url = reverse("classify")

        # Mock the NaiveBayesClassifier
        with patch.object(NaiveBayesClassifier, "classify", return_value=1):
            response = self.client.post(
                url,
                json.dumps({"classifier": "1", "content": "spam email"}),
                content_type="application/json",
            )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["prediction"], 1)

        # Mock the NaiveBayesClassifier
        with patch.object(NaiveBayesClassifier, "classify", return_value=1):
            response = self.client.post(
                url,
                json.dumps({"classifier": "0", "content": "spam email"}),
                content_type="application/json",
            )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["prediction"], 1)

        # Add more test cases for different scenarios

        response = self.client.get(url)
        self.assertEqual(response.status_code, 405)

    def tearDown(self):
        # Clean up any resources or data created during the tests
        # Unset the dynamic token after testing
        del os.environ["AUTH_TOKEN"]
