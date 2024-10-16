from django.contrib.auth import get_user_model
from django.test import SimpleTestCase, TestCase
from django.urls import reverse

class HomepageTests(SimpleTestCase):
    def test_url_exist_at_correct_location_homapage(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
    
    def test_homepage_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')
        self.assertContains(response, "Home")
        
class SignupPageTest(TestCase):
    def test_url_exist_at_correct_location_signup(self):
        response = self.client.get('/accounts/signup/')
        self.assertEqual(response.status_code, 200)
    
    def test_signup_view(self):
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/signup.html')
        self.assertContains(response, "Signup")
    
    def test_signup_form(self):
        response = self.client.post(
            reverse('signup'), 
            {
                'username': 'testuser',
                'email': 'testuser@gmail.com',
                'password1' : 'testpass123',
                'password2' : 'testpass123',
            },
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(get_user_model().objects.all().count(), 1)
        self.assertEqual(get_user_model().objects.all()[0].username, 'testuser')
        self.assertEqual(get_user_model().objects.all()[0].email, 'testuser@gmail.com')
        
class PreLogoutPageTest(SimpleTestCase):
    def test_url_exist_at_correct_location_homapage(self):
        response = self.client.get('/accounts/prelogout/')
        self.assertEqual(response.status_code, 200)
    
    def test_homepage_view(self):
        response = self.client.get(reverse('pre-logout'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/prelogout.html')
        self.assertContains(response, "Logout")