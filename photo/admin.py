from django.contrib import admin
#CustomUserをインポート
from .models import Category, PhotoPost

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')

class PhotoPostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title') 
    list_display_links = ('id', 'title')
    
#Django管理サイトにCategory,CategoryAdminを登録する
admin.site.register(Category, CategoryAdmin)
#Django管理サイトにPhotoPost,PhotoPostAdminを登録する
admin.site.register(PhotoPost, PhotoPostAdmin)      

# Register your models here.
