from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

class UserManager(BaseUserManager):
  def create_user(self, email, username, names, last_names, password, **other_fields):
    if not email:
      raise ValueError('El usuario debe tener un correo electronico')

    user=self.model(
                    username=username,
                    email=self.normalize_email(email),
                    names=names,
                    last_names=last_names,
                    **other_fields
                  )
    user.set_password(password)
    user.save()
    return user

  def create_superuser(self, username, names, last_names, email, password, **other_fields):
    other_fields.setdefault('is_staff', True)
    other_fields.setdefault('is_superuser', True)
    other_fields.setdefault('is_active', True)

    if other_fields['is_staff'] is not True:
      raise ValueError('El superusuario debe estar asignado como is_staff=True')
    if other_fields['is_superuser'] is not True:
      raise ValueError('El superusuario debe estar asignado como is_superuser=True')
    return self.create_user(
                            email,
                            username=username,
                            names=names,
                            last_names=last_names,
                            password=password,
                            **other_fields
                          )

# Create your models here.
class User(AbstractBaseUser, PermissionsMixin):
  username=models.CharField('Usuario', unique=True, max_length=20)
  #password
  names=models.CharField('Nombres', max_length=254, blank=True, null=True)
  last_names=models.CharField('Apellidos', max_length=254, blank=True, null=True)
  email=models.EmailField('Correo', max_length=254, unique=True)
  start_date=models.DateTimeField('Fch_creacion', default=timezone.now)
  is_staff=models.BooleanField('Staff', default=True)
  is_active=models.BooleanField('Estado', default=True)
  objects=UserManager()

  USERNAME_FIELD='username'
  REQUIRED_FIELDS=['email', 'names', 'last_names']

  def __str__(self):
    return f'{self.username} - {self.names}, {self.last_names}'

  # def has_perm(self, perm, obj=None):
  #   return True

  # def has_module_perms(self, app_label):
  #   return True

  # @property
  # def is_staff(self):
  #   return self.administrator