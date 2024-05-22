from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager



class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
   

    def __str__(self):
        return f"Nombre: {self.nombre}, Correo: {self.correo}, Contraseña: guardada"

class Usracceso(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    seed = models.CharField(max_length=40)

    #def __str__(self):
    #    return f"Nombre: {self.nombre}, Correo: {self.correo}, Contraseña: guardada , seed: {self.seed}"

class AccesoManager(BaseUserManager):
    def create_user(self, username, password=None):
        if not username:
            raise ValueError('El nombre de usuario es obligatorio')
        
        user = self.model(username=username)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None):
        user = self.create_user(username, password=password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class Dacceso(AbstractBaseUser):
    username = models.CharField(max_length=150, unique=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = AccesoManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    def has_perm(self, perm, obj=None):
        return self.is_superuser

    def has_module_perms(self, app_label):
        return self.is_superuser


class Acceso(models.Model):
    correo = models.EmailField(unique=True)
    password = models.CharField(max_length=100)

    def __str__(self):
        return f"Correo: {self.correo}, Contraseña: guardada"


class LoginUsuario(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    fecha_login = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Usuario: {self.usuario.nombre}, Fecha de Login: {self.fecha_login}"
