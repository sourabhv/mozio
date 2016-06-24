from time import timezone

from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.gis.db import models as geomodels
from django.core.mail import send_mail
from django.db import models
from django.utils.translation import ugettext_lazy as _


class ProviderManager(BaseUserManager):

    def _create_user(seld, email, password, is_staff, is_superuser, **extra_fields):
        '''Creates and saves a User with the given email and password'''
        now = timezone.now()

        if not email:
            raise ValueError('Email can\'t be empty')
        email = self.normalize_email(email)
        user = self.model(email=email, is_active=True, is_superuser=is_superuser,
                          is_staff=is_staff, last_login=now, date_joined=now,
                          **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password, **extra_fields):
        return self._create_user(email, password, False, False, **extra_fields)

    def create_user(self, email, password, **extra_fields):
        return self._create_user(email, password, True, True, **extra_fields)


class Provider(AbstractBaseUser):

    name = models.CharField(max_length=256)
    email = models.EmailField(max_length=256, unique=True, db_index=True)
    phone_number = models.CharField(max_length=32, unique=True)
    language = models.CharField(max_length=8)
    currency = models.CharField(max_length=8)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'phone_number', 'language', 'currency',]

    objects = ProviderManager()

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

    def __unicode__(self):
        return self.email

    def get_full_name(self):
        return self.name

    def get_short_name(self):
        return self.name

    def email_user(self, subject, message, from_email=None, **kwargs):
        send_mail(subject, message, from_email, [self.email])


class Area(geomodels.Model):
    provider = geomodels.ForeignKey(settings.AUTH_USER_MODEL, related_name='areas',
                                 on_delete=models.CASCADE)
    geojson = geomodels.PolygonField
    name = geomodels.CharField(max_length=256)
    price = geomodels.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = 'area'
        verbose_name_plural = 'areas'

    def __unicode__(self):
        return self.name

