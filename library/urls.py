from django.urls import path, include
from rest_framework.routers import DefaultRouter
from library.views import (
    AdminSignupView, admin_login, BookViewSet,
    student_book_list, book_list
)
from rest_framework.authtoken.views import obtain_auth_token


router = DefaultRouter()
router.register(r'books', BookViewSet, basename='book')

urlpatterns = [
    path('admin/signup/', AdminSignupView.as_view(), name='admin-signup'),
    path('admin/login/', admin_login, name='admin-login'),

   
    path('books/', book_list, name='book-list'), 


    path('student/books/', student_book_list, name='student-book-list'),
    path('token-auth/', obtain_auth_token, name='api-token-auth'),

  
    path('api/', include(router.urls)),
]
