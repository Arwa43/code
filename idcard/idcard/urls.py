from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from nationalcard import views
from rest_framework.authtoken.views import obtain_auth_token
router = DefaultRouter()


urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', views.register),
    path('get_user_info/', views.get_user_info),
    path('card_info/', views.card_info),
    
    path('Payment_info/', views.Payment_infos),
    path('Payment_confirmation/', views.Payment_confirmation),
    path('get_user_request/', views.get_user_request),
    path('get_user_datails/', views.get_user_datails), 
    path('show_my_report/', views.show_my_report),
    path('token/', obtain_auth_token),
    path('get_token/', views.get_token),
    #path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
