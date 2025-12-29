
"""
Django Database Model.
Docstring for app.core.models
"""
from django.db import models
from django.contrib.auth.models import (
     AbstractBaseUser,
     BaseUserManager,
     PermissionsMixin,
)


class UserManager(BaseUserManager):
     """ User Manager Models User. """
     
     def create_user(self,email,password=None,**extra_field):
          """ Create , save and Return New User."""
          if not email:
               raise ValueError('User Must have have an Email address. ')
          user=self.model(email=self.normalize_email(email), **extra_field)
          user.set_password(password)
          user.save(using=self._db )
          
          return user
     
     
     def create_superuser(self, email, password):
          """ Create superuser and Loging"""
          user = self.create_user(email, password)

          user.is_staff = True
          user.is_superuser = True
          user.save(using=self._db)

          return user

class User(AbstractBaseUser,PermissionsMixin):
     """ User In this System. """
     
     email=models.EmailField(max_length=255, unique=True)
     name=models.CharField(max_length=255)
     is_active=models.BooleanField(default=True)
     is_staff=models.BooleanField(default=False)
     
     objects=UserManager()
     
     USERNAME_FIELD="email"
     
     
     