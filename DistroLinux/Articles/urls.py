from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="main"),
    path('add-article/', views.add_article, name="add-article"),
    path('article/<slug:theme>/<int:article_pk>/', views.show_article, name="show-article"),
    path('article/<slug:theme>/page/<int:page_id>', views.open_theme_page, name="theme-page"),
    path('article/page/<int:page_id>', views.show_pages, name="show-pages"),
    path('register/', views.show_register_page, name="show-register-page"),
    path('login/', views.login_request, name="login-request"),
    path('logout/', views.logout_from_account, name="logout"),
    path('user/<int:user_pk>/<str:username>', views.logged_user_page, name="logged-user-page"),
    path('user/<int:user_pk>/<str:username>/edit', views.change_profile, name="change-profile-page"),
]