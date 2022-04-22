from django.contrib import admin
from django.contrib.auth import admin as auth_admin, get_user_model

UserModel = get_user_model()


@admin.register(UserModel)
class BookbarUserAdmin(auth_admin.UserAdmin):
    list_display = ('email', 'is_staff', 'date_joined')
    list_filter = ('is_staff', 'is_superuser', 'groups')
    ordering = ('email',)
    search_fields = ('email', )
    readonly_fields = ('date_joined', )

    fieldsets = (
        (None, {
            'fields': ('email', 'password')
        }),
        ('Permissions', {
            'fields': ('is_staff', 'is_superuser', 'groups', 'user_permissions')
        }),
        ('Important dates', {
            'fields': ('last_login', 'date_joined')
        }),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )


