from django.urls import path, include
from django.contrib import admin

api_urls = [
    path('user/', include('user.urls', namespace='user')),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(api_urls)),
]