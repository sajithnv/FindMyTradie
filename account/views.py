from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,PasswordChangeForm
from django.contrib.auth import login,authenticate,update_session_auth_hash
from mainApp.models import *
from django.contrib import messages
# Create your views here.
def signup(request):
	t1=UserCreationForm(request.POST or None)
	if t1.is_valid():
		t1.save()
		u=t1.cleaned_data.get('username')
		p=t1.cleaned_data.get('password1')
		user=authenticate(username=u,password=p)
		login(request,user)
		return redirect('mainApp1:index1')
	return render(request,'signup.html',{'form':t1})

def change_password(request):
	user_in=False
	emp_in=False
	u_name = request.user.username
	emp_status = emp_register.objects.filter(e_name=u_name,available=True)
	registered_user_data = user_register.objects.filter(u_name=u_name)
	if registered_user_data:
		user_in=True
	registered_emp_data = emp_register.objects.filter(e_name=u_name)
	if registered_emp_data:
		emp_in=True
	if request.method == 'POST':
		form = PasswordChangeForm(request.user, request.POST)
		if form.is_valid():
			user = form.save()
			update_session_auth_hash(request, user)  # Important!
			messages.success(request, 'Your password was successfully updated!')
			return redirect('mainApp1:index1')
	else:
		form = PasswordChangeForm(request.user)
	return render(request, 'change_password.html', {'form': form,'user_in1':user_in,'emp_in1':emp_in,'u_name':u_name,'emp_status1':emp_status})