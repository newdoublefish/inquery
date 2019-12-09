import xadmin
from xadmin import views
from xadmin.plugins.batch import BatchChangeAction
from .models import Department, UserProfile

# https://www.cnblogs.com/lyq-biu/p/9513888.html


class GlobalSetting(object):
    site_title = "POWER"
    site_footer = "POWER 2019"


class DepartmentAdmin(object):
    list_display = ['name', 'code', 'remark']


class UserAdmin(object):
    def fname(self, obj):
        return "%s%s" % (obj.firstname, obj.lastname)
    fname.short_description = "名字"
    fname.allow_tags = True
    fname.is_column = True
    list_display = ['username', 'fname', 'dep']
    list_filter = ['dep']


xadmin.site.register(views.CommAdminView, GlobalSetting)
# xadmin.site.unregister(UserProfile)
xadmin.site.register(Department, DepartmentAdmin)
# xadmin.site.register(UserProfile, UserAdmin)

