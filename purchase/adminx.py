import xadmin
from xadmin import views
from xadmin.plugins.batch import BatchChangeAction
from .models import Purchase

# https://www.cnblogs.com/Jirison/p/8656228.html


class PurchaseAdmin(object):
    import_excel = True
    list_display = ['material_code', 'manufacturer']
    search_fields = ['manufacturer', 'material_code', ]

    def post(self, request, *args, **kwargs):
        if 'excel' in request.FILES:
            pass
        return super(PurchaseAdmin, self).post(request, args, kwargs)


xadmin.site.register(Purchase, PurchaseAdmin)