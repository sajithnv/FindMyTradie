from django import forms
from mainApp.models import *

class f_user_register(forms.ModelForm):
    class Meta:
        model = user_register
        fields = ['u_name','phone_number','address']
class f_user_register_for_update(forms.ModelForm):
    class Meta:
        model = user_register
        fields = ['whatsapp_number','address']
class f_emp_register(forms.ModelForm):
    class Meta:
        model = emp_register
        fields = ['e_name','phone_number','e_img','address','location','service_name','certificate_img','available']
class f_emp_register_for_update(forms.ModelForm):
    class Meta:
        model = emp_register
        fields = ['e_img','address','location','service_name','certificate_img','available']
class f_services(forms.ModelForm):
    class Meta:
        model = services
        fields = ['u_name','e_name','requested','paid','accepted','working','completed','cancelled','feedback']




