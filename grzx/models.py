from django.db import models
from django.contrib import admin
from django import forms


class BlogBody(models.Model):
    blog_title = models.CharField(max_length=50)
    blog_body = models.TextField()
    blog_type = models.CharField(max_length=50)
    blog_timestamp = models.DateTimeField()
    blog_imgurl = models.CharField(max_length=50, blank=True, null=True)
    blog_author = models.CharField(max_length=20, null=True)
    blog_ismarkdown = models.CharField(max_length=1, null=True)
    blog_like = models.IntegerField(null=True)
    blog_clicknum = models.IntegerField(null=True)


class UserInfo(models.Model):
    nickname = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    work = models.CharField(max_length=20)
    company = models.CharField(max_length=50)
    email = models.CharField(max_length=20)

class UploadFileForm(models.Model):
    title = models.CharField(max_length=50)
    filePath = models.CharField(max_length=20)
    file = models.FileField()

class UserInfoForm(forms.Form):
    class Meta:
        module = UserInfo
        fields = '__all__'
    nickname = forms.CharField(required=True,max_length=20,error_messages={'required':'用户名不能为空'})
    password = forms.CharField(required=True,
                               min_length=6,
                               max_length=10,
                               error_messages={'required':'密码不能为空','min_length':'密码至少为6位，最多不超过10位'})
    work = forms.CharField(max_length=20,required=False)
    company = forms.CharField(max_length=50,required=False)
    email = forms.CharField(max_length=20,required=False)

# admin.site.register(BlogBody)
# admin.site.register(UserInfo)
# admin.site.register(UploadFileForm)
