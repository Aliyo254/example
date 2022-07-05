from django.urls import path
from .views import *

urlpatterns = [
    path('elder/register', RegElderView.as_view()),
    path('resident/register', RegResidentView.as_view()),
    path('controller/register', RegControllerView.as_view()),
    path('login/', CustomAuthToken.as_view(), name='auth-token'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('elder/home/', ElderOnlyView.as_view(), name='elder'),
    path('resident/home/', ResidentOnlyView.as_view(), name='resident'),
    path('controller/home/', ControllerOnlyView.as_view(), name='controller'),
    path('hoods/', Hood.as_view(), name='hood'),
    path('hood-details/<pk>', HoodDetail.as_view(), name='hood_detail'),
]