import xadmin
from xadmin import views
from xadmin.plugins.batch import BatchChangeAction
from .models import Purchase


class PurchaseAdmin(object):
    list_display = ['material_code']


xadmin.site.register(Purchase, PurchaseAdmin)