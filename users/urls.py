from django.urls import path
from .views import RegisterView, LoginView, LogoutView, ProfileView, DeleteUserView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),  # 회원가입
    path('login/', LoginView.as_view(), name='login'),  # 로그인
    path('logout/', LogoutView.as_view(), name='logout'),  # 로그아웃
    path('profile/', ProfileView.as_view(), name='profile'),  # 프로필 관리
    path('delete/', DeleteUserView.as_view(), name='delete_user'),  # 계정 삭제
]
