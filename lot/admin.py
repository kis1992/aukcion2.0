from django.contrib import admin
from lot import models
from mptt import admin as mptt_admin

# Register your models here.

class CategoryAdmin(mptt_admin.DraggableMPTTAdmin):
    pass

class LotAdmin(admin.ModelAdmin):
    filter_horizontal=('categories', )

admin.site.register(models.Category, CategoryAdmin)
admin.site.register(models.Lot, LotAdmin)
admin.site.register(models.Price)
