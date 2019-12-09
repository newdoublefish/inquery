from django.db import models
from django.contrib.auth.models import AbstractUser


class Department(models.Model):
    code = models.CharField(u'编号', default='', max_length=120, null=True, blank=True)
    name = models.CharField(u'名称', default='', max_length=120, null=False, blank=False)
    remark = models.CharField(u'备注', default='', max_length=200, null=True, blank=True)

    def __str__(self):
        return "%s" % self.name

    class Meta:
        verbose_name = "部门"
        verbose_name_plural = "部门"


class UserProfile(AbstractUser):
    dep = models.ForeignKey(Department, on_delete=models.CASCADE, verbose_name="部门", null=True, default=None)
    mobile = models.CharField(u'手机', max_length=11, default='')

    def __str__(self):
        return self.username