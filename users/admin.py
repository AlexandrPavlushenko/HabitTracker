from django.contrib import admin

from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "email", "username", "phone", "avatar", "telegram_chat_id")
    list_editable = ("username", "phone", "avatar", "telegram_chat_id")
    search_fields = ("username", "email")
