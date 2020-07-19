from django.urls import path,include,re_path
from device import views
urlpatterns = [
    path('',views.DeviceView.as_view()),
    path('<int:pk>/conf',views.DeviceConfView.as_view())
]