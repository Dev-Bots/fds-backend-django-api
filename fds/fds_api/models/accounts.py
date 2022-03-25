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