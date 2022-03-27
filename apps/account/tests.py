from django.contrib.auth import get_user_model
from django.test import TestCase


class UsersManagersTests(TestCase):
    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(email="py@mail.com", firstname="Paa", lastname="Yaw", password="test123")
        self.assertEqual(user.email, "py@mail.com")
        self.assertEqual(user.firstname, "Paa")
        self.assertEqual(user.lastname, "Yaw")
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertEqual(str(user), user.email)

        with self.assertRaises(ValueError):
            User.objects.create_user(email=None, password="test123")

    def test_create_superuser(self):
        User = get_user_model()
        superuser = User.objects.create_superuser(email="py@mail.com", password="test123")
        self.assertTrue(superuser.is_staff)
        self.assertTrue(superuser.is_active)
        self.assertTrue(superuser.is_superuser)

        with self.assertRaises(ValueError):
            User.objects.create_superuser(email="py@mail.com", password="test123", is_staff=False)
        with self.assertRaises(ValueError):
            User.objects.create_superuser(email="", password="test123")
        with self.assertRaises(ValueError):
            User.objects.create_superuser(email="py@mail.ocm", password="test123", is_superuser=False)
