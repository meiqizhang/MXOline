from django.db import models
from apps.users.models import UserProfile
from apps.users.models import BaseModel
# Create your models here.

class City(BaseModel):
    name = models.CharField(verbose_name="城市名",max_length=50)
    desc = models.CharField(verbose_name="城市描述",max_length=300)

    class Meta:
        verbose_name="城市信息"
        verbose_name_plural=verbose_name

    def __str__(self):
        return self.name

class CourseOrg(BaseModel):
    name = models.CharField(max_length=100,verbose_name="机构名称")
    title = models.CharField(max_length=300,verbose_name="机构标签")
    type = models.CharField(verbose_name="机构类型",choices=(("gr","个人"),("gx","高校")),max_length=2)
    fav_nums = models.IntegerField(verbose_name="收藏人数", default=0)
    click_nums = models.IntegerField(verbose_name="点击数", default=0)
    image = models.ImageField(upload_to="org/%Y/%m", verbose_name="logo", max_length=100)
    adress = models.CharField(max_length=100,verbose_name="机构地址")
    study_number = models.IntegerField(default=0,verbose_name="学习人数")
    course_number = models.IntegerField(default=0,verbose_name="课程数")
    is_authentication = models.BooleanField(default=0,verbose_name="是否认证")
    is_mdeal = models.BooleanField(default=0,verbose_name="是否金牌")
    city = models.ForeignKey(City, on_delete=models.CASCADE, verbose_name="所在城市")

    class Meta:
        verbose_name="机构信息"
        verbose_name_plural=verbose_name

    def __str__(self):
        return self.name

class Teacher(BaseModel):
    user = models.OneToOneField(UserProfile, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="用户")
    subsidiary_organ = models.CharField(max_length=100,verbose_name="所属机构")
    name = models.CharField(verbose_name="教师名称",max_length=50)
    work_years = models.IntegerField(verbose_name="工作年限",default=0)
    employ_company = models.CharField(verbose_name="就职公司",max_length=200)
    company_post = models.CharField(verbose_name="公司职位",max_length=100)
    teach_character = models.CharField(verbose_name="教学特点",max_length=500)
    click_nums = models.IntegerField(verbose_name="点击数",default=0)
    fav_nums = models.IntegerField(verbose_name="收藏数",default=0)
    years = models.IntegerField(verbose_name="年龄",default=0)
    image = models.ImageField(upload_to="teacher/%Y/%m", verbose_name="头像", max_length=100)

    class Meta:
        verbose_name="教师信息"
        verbose_name_plural=verbose_name

    def __str__(self):
        return self.name