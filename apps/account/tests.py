from django.contrib.auth import get_user_model
from django.test import TestCase


class UsersManagersTests(TestCase):
    def test_create_user(self) -> None:
        User = get_user_model()
        user = User.objects.create_user(
            email="py@mail.com",
            firstname="Paa",
            lastname="Yaw",
            password="test",
        )
        self.assertEqual(user.email, "py@mail.com")
        self.assertEqual(user.firstname, "Paa")
        self.assertEqual(user.lastname, "Yaw")
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertEqual(str(user), user.email)

        with self.assertRaises(ValueError):
            User.objects.create_user(
                email=None,
                firstname="Paa",
                lastname="Yaw",
                password="test123",
            )

    def test_create_superuser(self) -> None:
        User = get_user_model()
        superuser = User.objects.create_superuser(
            email="super@user.com",
            firstname="Super",
            lastname="User",
            password="test123",
        )
        self.assertTrue(superuser.is_staff)
        self.assertTrue(superuser.is_active)
        self.assertTrue(superuser.is_superuser)

        with self.assertRaises(ValueError):
            User.objects.create_superuser(
                email="super@user.com",
                firstname="Super",
                lastname="User",
                password="test123",
                is_staff=False,
            )
        with self.assertRaises(ValueError):
            User.objects.create_superuser(
                email="",
                firstname="Super",
                lastname="User",
                password="test123",
            )
        with self.assertRaises(ValueError):
            User.objects.create_superuser(
                email="super@user.ocm",
                firstname="Super",
                lastname="User",
                password="test123",
                is_superuser=False,
            )
