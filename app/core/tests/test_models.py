from django.test import TestCase
from django.contrib.auth import get_user_model

from core import models


def sample_user(email='test@test.com', password='112323'):
    """fsdfs"""
    return get_user_model().objects.create_user(email, password)


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

    def test_tag_str(self):
        """dfsdfdsfs"""
        tag = models.Tag.objects.create(
            user=sample_user(),
            name="vegan"
        )

        self.assertEqual(str(tag), tag.name)

    def test_ingredient_str(self):
        """Test the ingredient string representation"""
        ingredient = models.Ingredient.objects.create(
            user=sample_user(),
            name='Cucumber'
        )

        self.assertEqual(str(ingredient), ingredient.name)
