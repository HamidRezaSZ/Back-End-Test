from __future__ import unicode_literals
from django.contrib.auth import get_user_model
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import CustomUser
from .forms import CustomUserCreationForm

User = get_user_model()


class CustomUserAdmin(BaseUserAdmin):

    add_form = CustomUserCreationForm
    model = User
    list_display = ('username','email','phone', 'is_staff', 'is_active')
    list_filter = ('username','email','phone','is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('email', 'password',),}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username','email','phone', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request, obj)






admin.site.register(CustomUser, CustomUserAdmin)


