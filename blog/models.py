from datetime import datetime
from django.db import models
from DjangoUeditor.models import UEditorField


# Create your models here.

class  Category(models.Model):
    """
    类别
    """
    CATEGORY_TYPE=(
        (1,"一级类别"),
        (2,"二级类别"),
        (3,"三级类别"),
        (4,"四级类别"),

    )

    name= models.CharField(default='',max_length=30,verbose_name="类别名",help_text="类别名")
    code=models.CharField(default='',max_length=30,verbose_name="类别code",help_text="类别code")
    desc=models.CharField(default='',max_length=200,verbose_name="类别描述",help_text="类别描述")
    category_type=models.CharField(choices=CATEGORY_TYPE,max_length=20,verbose_name="类目级别",help_text="类目级别")
    parent_category=models.ForeignKey("self",null=True,blank=True,verbose_name="父类别",help_text="父类别",
                                      related_name="sub_cat",on_delete=models.CASCADE)
    is_tab=models.BooleanField(default=False,verbose_name="是否导航",help_text="是否导航")
    createtime=models.DateTimeField(default=datetime.now,verbose_name="添加时间")

    class Meta:
        verbose_name = "类别"
        verbose_name_plural = verbose_name



    def __str__(self):
        return  self.name


class Article(models.Model):
    category = models.ForeignKey(Category, default='',verbose_name="类别", on_delete=models.CASCADE)
    title=models.CharField(max_length=150,verbose_name="标题")
    body=UEditorField(verbose_name="内容",imagePath="images/",null=True,blank=True,width=1000,height=500,
                      filePath="data/file",default="")
    createtime=models.DateTimeField(default=datetime.now,verbose_name="创建时间")

    class Meta:
        verbose_name = "文章"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title

class  ArticleImage(models.Model):
    """
    图片
    """

    title=models.ForeignKey(Article,verbose_name="文章",related_name="Images",on_delete=models.CASCADE)
    image=models.ImageField(upload_to="",verbose_name="图片",null=True,blank=True)
    image_url=models.CharField(max_length=300,null=True,blank=True,verbose_name="图片url")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="创建时间")


    class Meta:
        verbose_name = "文章图片"
        verbose_name_plural = verbose_name


    def __str__(self):
        return self.title.name

class  Banner(models.Model):
    """
    首页轮播图
    """

    title=models.ForeignKey(Article,verbose_name="文章",on_delete=models.CASCADE)
    image=models.ImageField(upload_to="banner/",verbose_name="轮播图片")
    index=models.IntegerField(default=0,verbose_name="轮播顺序")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="创建时间")

    class Meta:
        verbose_name = "轮播图片"
        verbose_name_plural = verbose_name


    def __str__(self):
        return self.title.name