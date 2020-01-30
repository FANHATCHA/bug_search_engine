# from django.contrib import admin
# from django.urls import path, include
#
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     url(r'^posts/', include('posts.urls')),
# ]

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('posts', include('posts.urls')),
    path('admin/', admin.site.urls),
]