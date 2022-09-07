from django.contrib import admin
from .models import EmailSub, Email
# Register your models here.


class EmailSubAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'em_address')
    list_filter = ('id', 'first_name',)


class EmailAdmin(admin.ModelAdmin):
    list_display = ('id', 'subject', 'content')
    list_filter = ('id', 'subject',)


admin.site.register(EmailSub, EmailSubAdmin)
admin.site.register(Email, EmailAdmin)