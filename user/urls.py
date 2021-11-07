from django.urls import path, include

from .views import UserList, PasswordList, ChangePassword
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'user', UserList, basename='user')
router.register(r'password', ChangePassword, basename='change_password')
urlpatterns = [
    path('', include(router.urls)),
    path('<str:username>/', PasswordList.as_view()),
]

urlpatterns += router.urls
