from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.db.models import Q

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    password = serializers.CharField(max_length=30, write_only=True)
    confirm_password = serializers.CharField(max_length=30, write_only=True)

    class Meta:
        model = User
        fields = ('id', 'email','first_name' ,'last_name','password', 'confirm_password')


    def validate(self, attrs):
        confirm_password = attrs.get('confirm_password')

        if attrs.get('password') != confirm_password:
            raise serializers.ValidationError(
                "Password and Confirm_password doesn't match")

        # Validate password strength
        try:
            validate_password(confirm_password)
        except ValidationError as e:
            raise serializers.ValidationError(str(e))
        
        attrs.pop('confirm_password', None)
        return attrs

    def create(self, validated_data):
        user = User.objects.create_user(
            **validated_data
        )
        return user


class LoginSerializer(serializers.Serializer):
    '''Login with either username or email and password'''

    username = serializers.CharField(required=False,help_text='login with username.')
    email = serializers.EmailField(required=False,help_text='login with email')
    password = serializers.CharField(max_length=30, write_only=True)

    def validate(self, attrs):
        username = attrs.get('username')
        email = attrs.get('email')
        password = attrs.get('password')

        if (username or email) and password:
            user = User.objects.filter(Q(email=email) | Q(username=username)).first()
            if user:
                if user.check_password(password):
                    return attrs
                raise serializers.ValidationError('Invalid Password!')
            raise serializers.ValidationError('Invalid Email or Username!')
        raise serializers.ValidationError('Either Email or Password is required!')
