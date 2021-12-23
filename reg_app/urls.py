from django.urls import path  
from reg_app import views  


app_name = 'reg_app'
urlpatterns = [
	path('home/', views.home, name='home'),
	path('profile/', views.profile, name='profile'),
	path('signup/', views.signup, name='signup'),
	path('login/', views.login_page, name='login'),
	path('logout/', views.logout_page, name='logout')
]