from django.contrib import admin
from blog.models import Post, Category

# Register your models here.
class PostAdmin(admin.ModelAdmin) :
    emplty_value_display = '-empty-'
    exclude = ('published_date',)
    list_display = ('title','author' , 'status', 'counted_view','created_date', 'published_date')
    list_filter = ('status', 'author')
    search_fields = ['title','content']
    
admin.site.register(Category)
admin.site.register(Post,PostAdmin)
