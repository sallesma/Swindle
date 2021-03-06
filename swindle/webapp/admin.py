from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from webapp.models import TestData


class TestDataInline(admin.StackedInline):
    model = TestData
    can_delete = False
    verbose_name_plural = 'TestData'


class UserAdmin(UserAdmin):
    inlines = (TestDataInline, )


admin.site.unregister(User)
admin.site.register(User, UserAdmin)