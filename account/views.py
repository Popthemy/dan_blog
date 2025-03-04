from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate,login,logout
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .serializers import UserSerializer, LoginSerializer
from .permissions import IsAnonymous
from .reusable_func import get_jwt_tokens
# Create your views here.

User = get_user_model()


class UserRegisterView(GenericAPIView):
    '''Takes user valid data and returns a registered user data.'''

    serializer_class = UserSerializer
    permission_classes = [IsAnonymous]
    
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        token = get_jwt_tokens(user= serializer.save())

        data = {
            'status': 'Success',
            'message': 'Registration Successful',
            'token': token,
            'data': serializer.data
        }
        return Response(data=data, status=status.HTTP_201_CREATED)


class LoginView(GenericAPIView):
    '''Allows login with either email or password and return that user 
    access and refresh token
    '''

    serializer_class = LoginSerializer
    permission_classes = [IsAnonymous]

    def post(self, request):
        serializer = self.serializer_class(
            data=request.data, context={'request': request})

        if serializer.is_valid():
            user = serializer.validated_data

            serializer = UserSerializer(user)
            token = get_jwt_tokens(user=user)

            data = {
                'status': 'Success',
                'message': 'Welcome back👋',
                'token':token,
                'data': serializer.data
            }
            return Response(data=data, status=status.HTTP_200_OK)

        return Response(data={
            'status': 'Error',
            'message': 'Login Unsuccessful',
            'data': serializer.errors},
            status=status.HTTP_400_BAD_REQUEST)

