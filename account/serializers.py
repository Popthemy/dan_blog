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
        fields = ('id', 'username','email','first_name' ,'last_name','password', 'confirm_password')

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

    username_or_email = serializers.CharField(help_text='Enter your username or password.')
    password = serializers.CharField(max_length=30, write_only=True)

    def validate(self, attrs):
        username_or_email = attrs.get('username_or_email')
        password = attrs.get('password')

        # Check if required fields are provided
        if not username_or_email or not password:
            raise serializers.ValidationError('Both username/email and password are required.')

        # Fetch user by username or email
        user = User.objects.filter(Q(email=username_or_email) | Q(username=username_or_email)).first()

        # Validate user and password
        if user and user.check_password(password):
            return user
        else:
            # Generic error message to avoid exposing sensitive information
            raise serializers.ValidationError('Invalid credentials.')
