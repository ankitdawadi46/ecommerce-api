from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser
from rest_framework_simplejwt.tokens import RefreshToken

from .managers import CustomUserManager
from .constants import AUTH_PROVIDERS

# Base model for the user

class User(AbstractUser):

    username = None
    email = models.EmailField(_('email address'), unique=True)
    first_name = models.CharField(max_length=150, blank=True)
    last_name = models.CharField(max_length=150, blank=True)
    profile_pic = models.ImageField(upload_to='image',
                                    blank=True,
                                    null=True,
                                    default="/media/profile_pic.jpg")
    is_verified = models.BooleanField(default=False,
                                      blank=True,
                                      null=True)
    auth_provider = models.CharField(max_length=255,
                                     blank=False,
                                     null=False,
                                     default=AUTH_PROVIDERS.get('email'))
    is_active = models.BooleanField(default=False,
                                    blank=True,
                                    null=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email

    def tokens(self):
        refresh = RefreshToken.for_user(self)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token)
        }


class web_users(models.Model):
    user_details = models.OneToOneField(User, on_delete=models.CASCADE)
    ip = models.CharField(null=True, max_length=50)
    status = models.CharField(null=True, max_length=50)
    activation_code = models.CharField(max_length=50, default="code")
    forgetcode = models.CharField(max_length=50, null=True)
    forgetCodeSentTime = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.user_details.email

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def as_dict(self):
        return {
            "id":self.id,
            "ip":self.ip,
            "status":self.status,
            "activation_code":self.activation_code,
            "forgetcode":self.forgetcode,
            "forgetCodeSentTime":self.forgetCodeSentTime,
            "user_details":self.user_details
            }


class useraddress(models.Model):
    user = models.ForeignKey(web_users, on_delete=models.CASCADE)
    country_code = models.CharField(default="+977", max_length=10)
    contactno1 = models.CharField(default="9999999999", max_length=20)
    contactno2 = models.CharField(null=True, max_length=20)
    addressline1 = models.CharField(default="Kalanki", max_length=100)
    addressline2 = models.CharField(null=True, max_length=100)
    latitude = models.FloatField(null=True, max_length=50)
    longitude = models.FloatField(null=True, max_length=50)
    city = models.CharField(default="Kathmandu", max_length=50)
    province = models.CharField(default="Province 3", max_length=50)
    location_type = models.CharField(default="inside ringroad", max_length=50,
                                     null=False, blank=False)

    def __str__(self):
        return self.user.user_details.email

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def as_dict(self):
        return{
            "id":self.id,
            "user":self.user,
            "country_code":self.country_code,
            "contactno1":self.contactno1,
            "contactno2":self.contactno2,
            "addressLine1":self.addressline1,
            "addressLine2":self.addressline2,
            "latitude":self.latitude,
            "longitude":self.longitude,
            "city":self.city,
            "province":self.province,
        }


class unregistered_users(models.Model):
    email = models.CharField(default="ankitdawadi@gmail.com", max_length=50,
                             null=False, blank=False)
    contactno = models.CharField(default="9999999999", max_length=20,
                                 null=False, blank=False)
    full_name = models.CharField(default="Ankit Dawadi", max_length=50,
                                 null=False, blank=False)
    street_address = models.CharField(default="Kalanki", max_length=50,
                                      null=False, blank=False)
    city = models.CharField(default='Kathmandu', max_length=50,
                            null=False, blank=False)
    province = models.CharField(default="Bagmati", max_length=50,
                                null=False, blank=False)
    location_type = models.CharField(default="inside ringroad", max_length=50,
                                     null=False, blank=False)
