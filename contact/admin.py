from django.contrib import admin

from contact.models import Contact


class ContactAdmin(admin.ModelAdmin):
    list_display = ('subject', 'name', 'email', 'phone', 'date_submitted')

admin.site.register(Contact, ContactAdmin)
