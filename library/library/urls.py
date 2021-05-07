from django.contrib import admin
from django.urls import path, include
from user import views as user_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', include('digital_library.urls')),
    path('signup/', user_views.signup, name='signup'),
    path('admin/', admin.site.urls),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout')
    
]

handler404 = 'digital_library.views.not_found_404'
handler500 = 'digital_library.views.server_error_500'