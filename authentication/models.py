from django.db import models

from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
 
# Create your models here.

class CustomerUserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError("Email must be provided")
        
        if not password:
            raise ValueError("Password is requried")
        
        user = self.model(
            email=self.normalize_email(email),
        )
        
        user.set_password(password)
        user.save(using=self._db)
        
        return user
    
    def create_superuser(self, email, password=None):
        user = self.create_user(email, password)
        user.is_admin = True
        user.is_superuser = True
        
        user.save(using=self._db)
        
        return user
    


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    firstname = models.CharField(max_length=50,blank=True, null=True)
    lastname = models.CharField(max_length=50, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    
    objects = CustomerUserManager()
    
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    def __str__(self) -> str:
        return self.email
    
    @property
    def fullname(self):
        return f"{self.firstname} {self.lastname}"
    
    @property
    def is_staff(self):
        return self.is_admin
    
    
    
    
    