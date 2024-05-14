from django.test import TestCase
from django.urls import reverse

from .models import Post

class PostTests(TestCase): 
    @classmethod
    # Populates a dummy test data in separate db
    def setUpTestData(cls):
        cls.post = Post.objects.create(text="This is a test!")

    # Test if the db has newly entered dummy data
    def test_model_content(self): 
        self.assertEqual(self.post.text, "This is a test!")

    # Check if the url is set correctly
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/") 
        self.assertEqual(response.status_code, 200)

    
    # Same as above but checks based on the name which is defined in posts/urls.py
    def test_url_available_by_name(self): 
        response = self.client.get(reverse("home")) 
        self.assertEqual(response.status_code, 200)

    # Checks if the correct template is being used
    def test_template_name_correct(self):
        response = self.client.get(reverse("home")) 
        self.assertTemplateUsed(response, "home.html")

    # Checks cnotent of the template. in our case home.html
    def test_template_content(self):
        response = self.client.get(reverse("home")) 
        self.assertContains(response, "This is a test!")

    # Last three test cases from above combined into one unit test.
    # def test_homepage(self):
    #     response = self.client.get(reverse("home")) 
    #     self.assertEqual(response.status_code, 200) 
    #     self.assertTemplateUsed(response, "home.html") 
    #     self.assertContains(response, "This is a test!")
