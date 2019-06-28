from django.contrib import admin
from . import models
# Register your models here.

class CustomerAdmin(admin.ModelAdmin):
	list_display = [field.name for field in models.Customer._meta.fields]
	exclude = ['instrument_purchase', 'house_no', 'address_line1', 'address_line2']
	class Meta:
		model = models.Customer

admin.site.register(models.Customer, CustomerAdmin)
