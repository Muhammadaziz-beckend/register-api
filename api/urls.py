from django.urls import path,include
from .ysge import swagger

urlpatterns = [
    path('auth/', include('rest_registration.api.urls')),
]

urlpatterns += swagger