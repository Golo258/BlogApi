from rest_framework.test import APITestCase, APIRequestFactory
from .views import PostListCreateView
from django.urls import reverse
from rest_framework import status
from django.contrib.auth import get_user_model


User = get_user_model()


class HelloWorldTestCase(APITestCase):
    def test_hello_world(self):
        response = self.client.get(reverse("home_page"))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["message"], "Hello World")


class PostListCreateTestCase(APITestCase):
    def setUp(self):
        self.url = reverse("list_posts")

    def authenticate(self):
        self.client.post(
            reverse("signup"),
            {
                "email": "jonathan@app.com",
                "password": "password##!123",
                "username": "jonathan",
            },
        )

        response = self.client.post(
            reverse("login"),
            {
                "email": "jonathan@app.com",
                "password": "password##!123",
            },
        )

        token = response.data["tokens"]["access"]

        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {token}")

    def test_list_posts(self):

        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, [])

    def test_post_creation(self):
        self.authenticate()

        sample_data = {"title": "Sample title", "content": "Sample content"}
        response = self.client.post(reverse("list_posts"), sample_data)
        print("Response content")
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["title"], sample_data["title"])0