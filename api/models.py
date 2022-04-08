from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.
class User(models.Model):
    class Sex(models.IntegerChoices):
        MAN = 1, _('男')
        WOMAN = 2, _('女')

    class Status(models.IntegerChoices):
        BLOCK = 0, _('锁定')
        NORMAL = 1, _('正常')

    id = models.BigAutoField(primary_key=True)
    account = models.CharField(max_length=60, null=True, help_text="账户")
    nickname = models.CharField(max_length=60, null=True, blank=True, help_text="用户昵称")
    password = models.CharField(max_length=255, null=True, help_text="账号密码")
    sex = models.PositiveSmallIntegerField(choices=Sex.choices, default=Sex.MAN, help_text="性别信息[1: 男, 2: 女]")
    email = models.CharField(max_length=120, null=True, blank=True, help_text="邮箱")
    phone = models.CharField(max_length=24, null=True, blank=True, help_text="电话")
    avatar = models.CharField(max_length=255, null=True, blank=True, help_text="头像信息")
    status = models.PositiveSmallIntegerField(choices=Status.choices, default=Status.NORMAL,
                                              help_text="用户状态[0: 被锁定, 1: 正常]")
    created_date = models.PositiveIntegerField(null=True, help_text="创建时间")
    updated_date = models.PositiveIntegerField(null=True, help_text="更新时间")
