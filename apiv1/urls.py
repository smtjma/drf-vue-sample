from django.urls import path, include
from rest_framework import routers

from . import views
router = routers.DefaultRouter()
router.register('user_id_table', views.User_id_tableViewSet)

app_name = 'apiv1'
urlpatterns = [
    path('', include(router.urls)),
    
]