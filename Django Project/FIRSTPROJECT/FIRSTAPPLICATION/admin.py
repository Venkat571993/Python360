from django.contrib import admin
from .models import CustomerDetail

# Register your models here.
@admin.register(CustomerDetail)
class UserAdmin(admin.ModelAdmin):
    list_display=['id','first_name','last_name','contact_number','City']

