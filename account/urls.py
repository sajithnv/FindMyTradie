from django.conf.urls import url
from account.views import signup,change_password
from django.contrib.auth import views as auth_views

urlpatterns=[
	url(r'^signup/$',signup,name='signup1'),
	url(r'^login/$',auth_views.LoginView.as_view(template_name='login.html'),name='login1'),
	url(r'^logout/$',auth_views.LogoutView.as_view(next_page='mainApp1:index1'),name='logout1'),
	url(r'^empProfile/password/$',change_password, name='change_password1'),
	url(r'^userProfile/password/$',change_password, name='change_password2'),
]