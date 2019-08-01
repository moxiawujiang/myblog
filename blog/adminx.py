
import xadmin
from  blog.models import Article,Category,Banner
# Register your models here.

class ArticleAdmin(object):
    list_display = ['title','body','createtime']
    style_fields = {"body": "ueditor"}


class CategoryAdmin(object):
    list_display = ['name','code','desc','category_type','parent_category','is_tab','createtime']
    list_filter = ["category_type", "parent_category", "name"]
    search_fields = ['name', ]

class BannerAdmin(object):
    list_display = ['title','image','index','add_time']


xadmin.site.register(Article,ArticleAdmin)
xadmin.site.register(Category,CategoryAdmin)
xadmin.site.register(Banner,BannerAdmin)
