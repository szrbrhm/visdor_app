from django.contrib import admin
from .models import Contact

# Register your models here.

class ContactAdmin(admin.ModelAdmin):
    list_display = (
        "name", 
        "email", 
        "phone_number", 
        "message", 
        "created_date"
    )
    
    list_filter = ["name",]
    search_fields = ["name__startswith",]

admin.site.register(Contact, ContactAdmin)


