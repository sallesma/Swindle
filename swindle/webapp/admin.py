from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from webapp.models import TestPassword


class TestPasswordInline(admin.StackedInline):
    model = TestPassword
    can_delete = False
    verbose_name_plural = 'test_password'


class UserAdmin(UserAdmin):
    inlines = (TestPasswordInline, )


admin.site.unregister(User)
admin.site.register(User, UserAdmin)