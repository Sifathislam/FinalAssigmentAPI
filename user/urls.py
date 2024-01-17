from django.urls import path, include
from . import views
from rest_framework import routers
router = routers.DefaultRouter()

router.register('list', views.UpdateUserProfileImage)
# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
    path('register/', views.RegisterViewSet.as_view(), name='register'),
    path('active/<uid64>/<token>/', views.activate, name='activate'),
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('logout/', views.UserLogoutView.as_view(), name='logout'),
    path('update-user/<int:pk>/', views.UpdateUser.as_view(), name='update-user'),
    path('update-profile-image/', views.UpdateUserProfileImage.as_view(), name='update-profile-image'),
]