from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass
    def __str__(self):
        return self.username


class Department(models.Model):
    pass
    def __str__(self):
        return self.department_name

class Issue(models.Model):
    pass
    def __str__(self):
        return self.issue_name
