from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User


class CustomUserAdmin(UserAdmin):
    search_fields = ("email", "firstname", "lastname", "middlename")
    list_display = ("email", "firstname", "lastname", "middlename", "is_active", "is_staff")
    ordering = ("-date_joined",)
    list_filter = ("is_staff", "is_superuser", "is_active")
    fieldsets = (
        (
            "Profile",
            {
                "fields": (
                    "email",
                    "firstname",
                    "lastname",
                    "middlename",
                    "date_of_birth",
                    "profile_picture",
                )
            },
        ),
        ("Permissions", {"fields": ("is_staff", "is_active", "is_superuser")}),
        ("Important dates", {"fields": ("last_login",)}),
        ("Groups", {"fields": ("groups",)}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "firstname",
                    "lastname",
                    "middlename",
                    "password1",
                    "password2",
                    "is_staff",
                    "is_active",
                ),
            },
        ),
    )


admin.site.register(User, CustomUserAdmin)
