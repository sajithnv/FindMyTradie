
from django.contrib import admin
from mainApp.models import *
# Register your models here.
class adminView_model_user_register(admin.ModelAdmin):
	list_display=['u_name','phone_number','address','date']

admin.site.register(user_register,adminView_model_user_register)

class adminView_model_emp_register(admin.ModelAdmin):
	list_display=['e_name','phone_number','e_img','address','location','service_name','certificate_img','available','verified','date']

admin.site.register(emp_register,adminView_model_emp_register)

# class adminView_model_services(admin.ModelAdmin):
# 	list_display=['u_name','e_name','requested','paid_accepted','working','completed','cancelled','feedback']

# admin.site.register(services,adminView_model_services)