from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """test creating a new user with an is successful"""
        email = "test@test.com"
        password = 'test123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """ test if new user is normalized"""
        email = "test@FSDFSDFSDF.com"
        user = get_user_model().objects.create_user(email, '12345')

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """test no email"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, '123')

    def test_create_new_super_user(self):
        """create super user"""
        user = get_user_model().objects.create_superuser(
            'test@test.com',
            '1234'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
