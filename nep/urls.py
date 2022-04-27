from django.urls import path
from . import views
urlpatterns = [
	path('', views.indexView, name='index'),
	path('about/', views.aboutView, name='about'),
	path('blog/', views.blogView, name='blog'),
	path('contacts/', views.contactsView, name='contacts'),
	path('user/signup', views.signupView, name='signup'),
	path('user/login', views.loginView, name='login'),
	path('nepgear_secret_site/', views.nepgear_secret_site, name='secret'),
	
]