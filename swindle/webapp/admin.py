from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from webapp.models import TestPassword, Host, HostParameter, SwindleTest


class TestPasswordInline(admin.StackedInline):
    model = TestPassword
    can_delete = False
    verbose_name_plural = 'test_password'


class UserAdmin(UserAdmin):
    inlines = (TestPasswordInline, )


class TestHostParameterInline(admin.StackedInline):
    model = HostParameter
    can_delete = True
    verbose_name_plural = 'Host login parameters'


class HostAdmin(admin.ModelAdmin):
    fields = ['name', 'connection_url', 'success_regexp', 'failure_regexp']
    list_display = ('name', 'connection_url', 'success_regexp', 'failure_regexp')
    inlines = (TestHostParameterInline, )


class SwindleTestAdmin(admin.ModelAdmin):

    def get_readonly_fields(self, request, obj=None):
        if obj: # this is an edit
            return ['result',]
        else: # This is an add
            return []


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Host, HostAdmin)
admin.site.register(SwindleTest, SwindleTestAdmin)