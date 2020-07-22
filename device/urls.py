from django.urls import path,include,re_path
from device import views
urlpatterns = [
    path('',views.DevicePostView.as_view()),
    path('<int:pk>/conf',views.DeviceConfView.as_view()),
    path('<int:pk>/unable',views.DeviceUnableView.as_view()),
    path('<int:pk>/update',views.DeviceupdateView.as_view()),
    path('list',views.DevicelistView.as_view()),
]