from django.db import models

class UserInfo(models.Model):
    user = models.CharField(verbose_name="用户名", max_length=32)
    pwd = models.CharField(verbose_name="密码", max_length=64)
    roleChoices = (
        ("admin", "管理员"),
        ("user", "用户"),
        ("manager", "经理"),
    )
    role = models.CharField(verbose_name="角色", choices=roleChoices, max_length=16, default="user")


class Depart(models.Model):
    title = models.CharField(verbose_name="部门名称", max_length=32)
    count = models.IntegerField(verbose_name="人数")


