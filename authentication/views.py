from rest_framework import generics, status, views, permissions
from .serializers import LoginSerializer,RegisterSerializer,ResetPasswordEmailRequestSerializer,SetNewPasswordSerializer
from rest_framework.response import Response
from django.contrib.auth import authenticate, login,logout
from django.contrib import auth
from rest_framework.authtoken.models import Token
from datetime import datetime
from django.contrib.auth.models import User
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import force_str,smart_str,smart_bytes,DjangoUnicodeDecodeError
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
from .utils import Util
# Create your views here.

class LoginAPIView(generics.GenericAPIView):
    serializer_class=LoginSerializer
    def login(request):
        email = request.data.get('email')
        password = request.data.get('password')
        if email is None or password is None:
            return Response({'error': 'Please provide both email and password'}, status=status.HTTP_400_BAD_REQUEST)
        
        user = auth.authenticate(email=email, password=password)
        if not user:
           return Response({'error': 'Invalid Credentials'}, status=status.HTTP_404_NOT_FOUND)
        
        token, _ = Token.objects.get_or_create(user=user)
        user.last_login = datetime.now()
        user.save()
        return Response({'token': {token.key}}, status=status.HTTP_200_OK)
    
    # def post(self,request):
    #     serializer=self.serializer_class(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     return Response(serializer.data,status=status.HTTP_200_OK)

class RegisterView(generics.GenericAPIView):

    serializer_class = RegisterSerializer
    
    def post(self, request):
        user = request.data
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        user_data = serializer.data
        
        
        # # user = User.objects.get(email=user_data['email'])
        # # token = RefreshToken.for_user(user).access_token
        # # current_site = get_current_site(request).domain
        # # relativeLink = reverse('email-verify')
        # # absurl = 'http://'+current_site+relativeLink+"?token="+str(token)
        # # email_body = 'Hi '+user.username + \
        # #     ' Use the link below to verify your email \n' + absurl
        # # data = {'email_body': email_body, 'to_email': user.email,
        #         'email_subject': 'Verify your email'}

        # # Util.send_email(data)
        
        return Response(user_data, status=status.HTTP_201_CREATED)
    
# RequestPasswordResetEmail
class RequestPasswordResetEmailView(generics.GenericAPIView):
    serializer_class = ResetPasswordEmailRequestSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        email = request.data.get('email')

        if User.objects.filter(email=email).exists():
            user = User.objects.get(email=email)
            uidb64 = urlsafe_base64_encode(smart_bytes(user.id))
            token = PasswordResetTokenGenerator().make_token(user)
            current_site = get_current_site(
                request=request).domain
            relativeLink = reverse(
                'password-reset-confirm', kwargs={'uidb64': uidb64, 'token': token})

            redirect_url = request.data.get('redirect_url', '')
            absurl = 'http://'+current_site + relativeLink
            email_body = 'Hello, \n Use link below to reset your password  \n' + \
                absurl+"?redirect_url="+redirect_url
            data = {'email_body': email_body, 'to_email': user.email,
                    'email_subject': 'Reset your passsword'}
            Util.send_email(data)
        return Response({'success': 'We have sent you a link to reset your password'}, status=status.HTTP_200_OK)
    
#set new password 

class SetNewPasswordAPIView(generics.GenericAPIView):
    serializer_class = SetNewPasswordSerializer

    def patch(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response({'success': True, 'message': 'Password reset success'}, status=status.HTTP_200_OK)



    