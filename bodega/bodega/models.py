from django.db import models
from django.dispatch import receiver
from allauth.account.signals import user_signed_up

class RegistroUsuario(models.Model):
    rol = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=40)
    contrasena = models.CharField(max_length=8)
    contrasenaVe = models.CharField(max_length=8)
    

class RegistroBodeguero(models.Model):
    nombre = models.CharField(max_length=40)
    email = models.CharField(max_length=50)
    rut = models.CharField(primary_key= True, max_length=18)
    fechaNac = models.CharField(max_length=8)
    contraseña = models.CharField(max_length =20)

@receiver(user_signed_up)
def create_user_profile(request, user, **kwargs):
    profile = Profile.objects.create(user=user)
    profile.save()