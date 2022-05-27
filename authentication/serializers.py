
import email
from rest_framework.exceptions import AuthenticationFailed
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout
from django.contrib import auth
from rest_framework.authtoken.models import Token
from datetime import datetime
from django.utils.encoding import force_str,smart_str
from base64 import urlsafe_b64decode
from django.contrib.auth.tokens import PasswordResetTokenGenerator
#Login 
class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['id','email','password','last_login']
        extra_kwargs={'password':{'write_only': True,'required':True}}
                     
                     
# Register New user    
class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
            required=True,
            validators=[UniqueValidator(queryset=User.objects.all())]
            )

    password = serializers.CharField(write_only=True, required=True)
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'password2', 'email','date_joined')
        

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
          
        )
        
        user.last_login = datetime.now()        
        user.set_password(validated_data['password'])
        Token.objects.create(user=user)   
        user.save()
        return user
#Reset Email
class ResetPasswordEmailRequestSerializer(serializers.Serializer):
    email=serializers.EmailField(min_length=2)
    redirect_url=serializers.CharField(max_length=00, required=False)
    class Meta:
        fields=['email']
        
#Email verify
class EmailVerificationSerializer(serializers.ModelSerializer):
    token=serializers.CharField(max_length=200)
    class Meta:
        model=User
        fields=['token']
        
#Set new password
class SetNewPasswordSerializer(serializers.Serializer):
    password=serializers.CharField( min_length=6, max_length=50, write_only=True)
    token=serializers.CharField(min_length=1, write_only=True)
    uidb64=serializers.CharField(min_length=1, write_only=True)
    class Meta:
        fields=['password', 'token', 'uidb64']
    def validate(self, attrs):
        try:
            password=attrs.get('password')
            token=attrs.get('token')
            uidb64=attrs.get('uidb64')
            id=force_str(urlsafe_b64decode(uidb64))
            user=User.objects.get(id=id)

            if not PasswordResetTokenGenerator().check_token(user,token):
                raise AuthenticationFailed('The reset ink is invalid',401)

            user.set_password(password)
            user.save()

            return (user)
        except Exception as e:
            raise AuthenticationFailed('The reset link is invalid', 401)
        return super().validate(attrs)
