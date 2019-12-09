from django.db import models
import datetime


def upload_to(instance, fileName):
    # print('/'.join(["record", instance.order.sn_text, fileName]))
    return '/'.join(["purchase", instance.material_code, fileName])


# Create your models here.
class Purchase(models.Model):
    material_code = models.CharField(u'制造商料号', default='', max_length=60, null=True, blank=True)
    inner_model = models.CharField(u'公司型号', default='', max_length=60, null=True, blank=True)
    categories = models.CharField(u'类型', default='', max_length=60, null=True, blank=True)
    manufacturer = models.CharField(u'制造商', default='', max_length=60, null=True, blank=True)
    suppliers = models.CharField(u'供应商', default='', max_length=60, null=True, blank=True)
    price = models.DecimalField(u'单价', max_digits=14, decimal_places=4, blank=True, null=True)
    unit = models.CharField(u'单位', default='', max_length=20, null=True, blank=True)
    currency = models.CharField(u'货币', default='', max_length=20, null=True, blank=True)
    package = models.DecimalField(u'包装量', max_digits=14, decimal_places=4, blank=True, null=True)
    delivery = models.DateTimeField('交期', default=datetime.datetime.now)
    order_quantity = models.DecimalField(u'订货量', max_digits=14, decimal_places=4, blank=True, null=True)
    rate = models.DecimalField(u'税率', max_digits=14, decimal_places=4, blank=True, null=True)
    remark = models.CharField(u'备注', default='', max_length=60, null=True, blank=True)
    path = models.CharField(u'存放路径', default='', max_length=200, null=True, blank=True)
    picture = models.FileField(u'报价图片', upload_to=upload_to, null=True)

    def __str__(self):
        return "%s" % self.material_code

    class Meta:
        verbose_name = "报价记录"
        verbose_name_plural = verbose_name
