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
    class Foot(models.TextChoices):
        RIGHT = "RIGHT", "Right"
        LEFT = "LEFT", "Left"
        BOTH = "BOTH", "Both"

    class PlayingPossition(models.TextChoices):
        GK = "GK"

        CB = "DEF/CB"
        RB = "DEF/RB"
        LB = "DEF/LB"

        CM = "MID/CM"
        LM = "MID/LM"
        RM = "MID/RM"
        CAM = "MID/CAM"
        CDM = "MID/CDM"

        CF = "STR/CF"
        LW = "STR/LW"
        RW = "STR/RW"

    gender = models.CharField(
        _("Gender"), max_length=50, choices=Gender.choices, blank=False
    )
    dob = models.DateField(_("Date of birth"), auto_now=False, auto_now_add=False, blank=False)

    overview = models.TextField(_("Overview"), blank=True)
    video = models.FileField(_("Video link"), blank=True, upload_to=VIDEO_PATH) 
    birth_certificate = models.FileField(_("Birth certificate"), blank=False, upload_to=BIRTH_CERTIFICATE_PATH)
    education_level =  models.CharField(_("Education level"), blank=False, max_length=255)
    highest_education_evidence = models.FileField(_("Education evidence"), blank=False, upload_to=EDUCATION_CERTIFICATE_PATH)

    foot = models.CharField(
        _("Preffered foot"), max_length=50, choices=Foot.choices, default=Foot.RIGHT
    )
    weight = models.FloatField(_("Weight"), blank=False)
    height = models.FloatField(_("Height"), blank=False)
    playing_possition1 = models.CharField(
        _("Playing possition 1"), max_length=50, choices=PlayingPossition.choices, blank=False
    )
    playing_possition2 = models.CharField(
        _("Playing possition 2"), max_length=50, choices=PlayingPossition.choices, blank=False
    )


class Player(Account):
    base_type = Account.Types.PLAYER
    objects = PlayerAccountManager()

    @property
    def more(self):
        return self.playermore

    class Meta:
        proxy = True



############ Club specific account #################
class ClubMore(models.Model):
    account = models.OneToOneField(Account, on_delete=models.CASCADE)

    #the additional fields
    club_name = models.TextField(_("Club name"), blank=True)
    acronym =models.TextField(_("Acronym"), blank=True)
    
    organization_type =models.TextField(_("Organization type"), blank=True)
    website = models.TextField(_("Website"), blank=True)
    establishment_year = models.DateField(_("Establishment year"), blank=True, max_length=255)
    
class Club(Account):
    base_type = Account.Types.CLUB
    objects = ClubAccountManager()

    @property
    def more(self):
        return self.clubmore

    class Meta:
        proxy = True

############ Scout specific account #################
class ScoutMore(models.Model):
    id = models.IntegerField(primary_key=True, unique=True, auto_created=False)
    account = models.OneToOneField(Account, on_delete=models.CASCADE)

    #the additional fields
    is_assigned = models.BooleanField(_("Is the Scout assigned"), default=False)

    gender = models.CharField(
        _("Gender"), max_length=50, choices=Gender.choices, blank=False
    )
    dob = models.DateField(_("Date of birth"), auto_now=False, auto_now_add=False, blank=False)
    club = models.ForeignKey("Club", on_delete=models.CASCADE, related_name='scouts')

     
class Scout(Account):
    base_type = Account.Types.SCOUT
    objects = ScoutAccountManager()

    @property
    def more(self):
        return self.scoutmore

    class Meta:
        proxy = True


############ Adminspecific account #################    
# class Admin(Account):
#     base_type = Account.Types.ADMIN
#     objects = AdminAccountManager()

#     class Meta:
#         proxy = True