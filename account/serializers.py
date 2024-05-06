from . models import UserAccount
from rest_framework import serializers
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
class UserAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAccount
        fields = ['id', 'user', 'account_no', 'balance', 'image']


class UserRegistrationSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(required=True)
    image = serializers.ImageField(required=True)
    
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password', 'confirm_password', 'image']
    
    def save(self):
        username = self.validated_data['username']
        email = self.validated_data['email']
        first_name = self.validated_data['first_name']
        last_name = self.validated_data['last_name']
        password = self.validated_data['password']
        password2 = self.validated_data['confirm_password']
        image = self.validated_data.pop('image')
        if password != password2:
            raise serializers.ValidationError({'error' : "Password doesn't match"})
        
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({'error' : "Email already exists"})
        user = User(username=username, email=email, first_name=first_name, last_name=last_name)
        print(user)
        
        user.set_password(password)
        user.is_active = False
        user.save()
        UserAccount.objects.create(user=user, image=image, balance=0, account_no=int(user.id) + 1000)
        return user
    
class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)
    
    
    
    
    
class UserProfileUpdateSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(required=False)
    
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'image']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance:
            try:
                user_account = self.instance.account
            except UserAccount.DoesNotExist:
                user_account = None
            if user_account:
                self.fields["image"].initial = user_account.image

    def save(self, **kwargs):
        commit = kwargs.pop("commit", True)
        data = super().save(**kwargs)

        if commit:
            data.save()

            user_account, created = UserAccount.objects.get_or_create(user=data)
            user_account.image = self.validated_data.get("image", None)
            user_account.save()

        return data
    
class PasswordChageSerializer(serializers.Serializer):
    user_id = serializers.IntegerField(required=True)
    old_password = serializers.CharField(write_only=True, required=True)
    password = serializers.CharField(write_only=True, required=True)
    password2 = serializers.CharField(write_only=True, required=True)

    def validate(self, data):
        user_id = data.get("user_id")
        old_password = data.get("old_password")
        password = data.get("password")
        password2 = data.get("password2")

        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            raise ValidationError("User not found")

        if not user.check_password(old_password):
            raise ValidationError("Old password is not correct")

        if password != password2:
            raise ValidationError("New passwords doesn't match")

        return data

    def save(self):
        user_id = self.validated_data["user_id"]
        password = self.validated_data["password"]

        user = User.objects.get(id=user_id)
        user.set_password(password)
        user.save()
        
class AllUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "first_name", "last_name", "email"]