from django.contrib import admin
from django.urls import path, include
from djoser.views import TokenCreateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('api/token/', TokenCreateView.as_view(), name='token_create'),  #создания токена
    path('api/', include('my_app.urls')),
]