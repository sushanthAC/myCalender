from django.contrib import admin
from django.urls import path
from meetings import views
from django.contrib.auth import views as auth_views

urlpatterns = [
	path('', views.index, name='index'),
	path('meetings', views.meetings, name='meetings'),
    path('signup/', views.signup, name="signup"),
    path('login/', auth_views.login, name="login"),
    path('logout/', auth_views.logout,{'next_page': '/login'}, name="logout"),
	path('meetings/<int:pk>', views.details, name='details'),
    path('admin/', admin.site.urls),
    path('meetings/add', views.add, name="add"),
    path('meetings/delete/<int:pk>', views.delete, name='delete')
]
