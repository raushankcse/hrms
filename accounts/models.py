from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class CustomUser(AbstractUser):
    email = models.EmailField(max_length=255, unique=True, blank=False)

    two_fa_enabled = models.BooleanField(default=False)
    two_fa_secret = models.TextField(null=True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email




class Roles(models.Model):
    name = models.CharField(max_length=255, blank=False)

    def __str__(self):
        return self.name


class UserRoles(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    role = models.ForeignKey(Roles, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'role')



class Permissions(models.Model):
    module = models.CharField(max_length=255, blank=False)
    action = models.CharField(max_length=255, blank=False)

    def __str__(self):
        return f"{self.module} | {self.action}"


class RolePermission(models.Model):
    role = models.ForeignKey(Roles, on_delete=models.CASCADE)
    permission = models.ForeignKey(Permissions, on_delete=models.CASCADE)
    class Meta:
        unique_together = ('role', 'permission')




