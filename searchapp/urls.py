from django.urls import path
from django.contrib import admin
from .views import SearchView,indexView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('search/',SearchView.as_view(), name='search'),
    path("",indexView.as_view(),name="index")
]