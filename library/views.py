from django.shortcuts import render

from rest_framework import generics, status, permissions
from rest_framework.response import Response
from django.contrib.auth import authenticate
from .models import AdminUser, Book
from .serializers import AdminUserSerializer, BookSerializer
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes


from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view

# Admin Signup API View
class AdminSignupView(generics.CreateAPIView):
    serializer_class = AdminUserSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            # Check duplicate email: serializer already enforces unique on email.
            user = serializer.save()
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Admin Login API View using token authentication
@api_view(['POST'])
@permission_classes([permissions.AllowAny])

def admin_login(request):
    email = request.data.get("email")
    password = request.data.get("password")
    user = authenticate(request, email=email, password=password)
    if user:
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key})
    return Response({'error': 'Invalid Credentials'}, status=status.HTTP_400_BAD_REQUEST)


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all().order_by('title')
    serializer_class = BookSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]


@api_view(['GET'])
def student_book_list(request):
    books = Book.objects.all().order_by('title')
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data)


def book_list(request):
    books = Book.objects.all().order_by('title')
    return render(request, 'library/book_list.html', {'books': books})
