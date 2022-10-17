from django.contrib import admin
from contact_form.models import Contact


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    pass