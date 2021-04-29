from django.contrib import admin
from django.contrib.auth.admin import UserAdmin


from .models import User


@admin.register(User)
class UserAdmin(UserAdmin):
    model = User
    list_display = ('username', 'email', 'is_active',)
    list_filter = ('sex', 'is_active',)
    fieldsets = (
        ("Account Information", {'fields': ('email', 'username','password')}),
        ("Profile Information", 
            {'fields': (
                'first_name', 
                'last_name', 
                'phone', 
                'sex', 
                'image_tag', 
                'profile'
                )
             }
        ),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_superuser', 'groups', 'user_permissions' )}),
    )
    add_fieldsets = (
        ("Account Information", {'fields': ('email', 'username','password1', 'password2')}),
        ("Profile Information", 
            {'fields': (
                'first_name', 
                'last_name',
                'phone', 
                'sex',  
                'image_tag', 
                'profile'
                )
             }
        ),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_superuser', 'groups', 'user_permissions' )}),
    )
    readonly_fields = ('image_tag',)
    ordering = ('username','first_name', 'email')
