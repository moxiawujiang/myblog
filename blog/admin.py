
from django.contrib import admin
from  blog.models import Article,Category,Banner
# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title','body','createtime']

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name','code','desc','category_type','parent_category','is_tab','createtime']

class BannerAdmin(admin.ModelAdmin):
    list_display = ['title','image','index','add_time']


admin.site.register(Article,ArticleAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Banner,BannerAdmin)
