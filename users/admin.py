from django.contrib import admin
from .models import Profile, Follow

admin.site.register(Profile)
admin.site.register(Follow)

class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'is_staff', 'is_active')
    actions = ['delete_selected_users']

    def delete_selected_users(self, request, queryset):
        for user in queryset:
            user.delete()
        self.message_user(request, "Selected users have been deleted.")
    delete_selected_users.short_description = "Delete selected users"