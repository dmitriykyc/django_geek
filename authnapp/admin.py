from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Register your models here.
from .models import ShopUser


class ShopUserAdmin(UserAdmin):
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("username", "password1", "password2", "age"),
            },
        ),
    )


admin.site.register(ShopUser, ShopUserAdmin)
