from django.urls import path
from .import views 
from contact.views import messages
app_name = 'accounts'

urlpatterns = [
	path('signup/', views.signup_views, name='signup'),
	path('login/', views.login_view, name='login'),
	path('logout/', views.logout_view, name='logout'),
	path('messages/', messages, name='messages'),
	path('profile/<username>', views.profile, name='profile'),
]