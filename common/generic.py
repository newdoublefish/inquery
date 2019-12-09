# from django.db import models
#
# class BO(models.Model):
#     create_date = models.CharField(_("creator"),blank=True,null=True,max_length=const.DB_CHAR_NAME_20)
#     modifier = models.CharField(_("modifier"),blank=True,null=True,max_length=const.DB_CHAR_NAME_20)
#     create_date = models.DateTimeField(_('creation'),auto_now_add=True,blank=True,null=True)
#     modification = models.DateTimeField(_('modification'),auto_now=True,blank=True,null=True)
#     # mine = MineBOManager()
#     objects = models.Manager()
#
#     def __unicode__(self):
#         display = getattr(self,'name',None) or getattr(self,'title',None) or getattr(self,'description',None)
#         if not display:
#             display = ' '
#         return '%s' % display
#
#     class Meta:
#         abstract = True