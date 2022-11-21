from django.contrib import admin
from website.models import Contact, Newsletter

# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    
    empty_value_display = '-empty-'
    list_display = ('name','subject','email','updated_date')
    search_fields = ('name','email')
    list_filter = ('updated_date',)

admin.site.register(Contact,ContactAdmin)
admin.site.register(Newsletter)

