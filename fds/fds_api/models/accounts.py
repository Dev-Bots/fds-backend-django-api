from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.hashers import make_password

# constants  !!!!!!!!! need to find a better place to put em
PROFILE_PICTURE_PATH = 'assests/images/profile_pictures/'
BIRTH_CERTIFICATE_PATH = 'assets/images/birth_certifcate/'
EDUCATION_CERTIFICATE_PATH = 'assets/images/education/'
VIDEO_PATH = 'assets/video/'

class Account(AbstractUser):
    class Types(models.TextChoices):
        PLAYER = "PLAYER", "Player"
        SCOUT = "SCOUT", "Scout"
        CLUB = "CLUB", "Club"
        ADMIN = "ADMIN"


    base_type = Types.ADMIN
    is_active = models.BooleanField(default=True)
    type = models.CharField(
        _("Type"), max_length=50, choices=Types.choices, default=base_type
    )

    phone_number = models.CharField(_("Phone number"), blank=False, max_length=255)
    email = models.EmailField(_("Email"), blank=False, max_length=255)
    profile_picture =  models.ImageField(_("Profile picture"), upload_to=PROFILE_PICTURE_PATH, blank=True)
    address = models.CharField(_("Address"), max_length=255, blank=False)
    
    

    USERNAME_FIELD = 'username'

    def get_absolute_url(self):
            return reverse("accounts:detail", kwargs={"username": self.username})

    def save(self, *args, **kwargs):
        if not self.id:
            self.type = self.base_type
        return super().save(*args, **kwargs)

class Gender(models.TextChoices):
    MALE = "MALE", "Male"
    FEMALE = "FEMALE", "Female"

# account managers for filtering the query set with the respective account types
class PlayerAccountManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(type=Account.Types.PLAYER)

class ScoutAccountManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(type=Account.Types.SCOUT)

# class AdminAccountManager(models.Manager):
    

#     def create_superuser(self, **validated_data):

#         validated_data['password'] = make_password(validated_data['password'])

#         validated_data['is_staff'] = True
#         validated_data['is_superuser'] = True
#         validated_data['is_active'] = True
#         # validated_data['phone_no'] = '0911'

#         if validated_data['is_staff'] is not True:
#             raise ValueError(
#                 'Superuser must be assigned to is_staff=True.')
#         return Account.objects.create(**validated_data)
        
#     def get_queryset(self, *args, **kwargs):
#         return super().get_queryset(*args, **kwargs).filter(type=Account.Types.ADMIN)

class ClubAccountManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(type=Account.Types.CLUB)

############ Player specific account #################
class PlayerMore(models.Model):

    account = models.OneToOneField(Account, on_delete=models.CASCADE)

