from django.contrib import admin
from django.urls import path

from games import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('halo/', views.halo),
    path('run/',views.run)
]

