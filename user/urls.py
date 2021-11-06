from django.urls import path, include

from .views import UserList, PasswordList, ChangePassword
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'user', UserList, basename='user')
router.register(r'password', ChangePassword, basename='change_password')
# router.register(r'showcategory', ShowCategoryList, basename='show_category')
urlpatterns = [
    # path('article/', ArticleList.as_view()),
    path('', include(router.urls)),

    # path('article/', ArticleList.as_view()),
]

urlpatterns += router.urls