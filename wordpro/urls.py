from django.contrib import admin
from django.urls import path
import wordapp.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',wordapp.views.home, name = "home"),
    path('about/',wordapp.views.about, name = "about"),
    path('result/',wordapp.views.result, name = "result"),
]
