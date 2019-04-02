from django.db import models
from django.contrib.auth import models as auth_models
from django.contrib.auth import get_user_model


# Create your models here.

UserModel = get_user_model()


class CustomGroup(auth_models.Group):
    team = models.ForeignKey('Team', null=True, on_delete=models.DO_NOTHING)
    permissions = models.ManyToManyField('GroupPermisison')


class GroupPermission(models.Model):
    name = models.TextField()


class Team(models.Model):
    name = models.CharField(max_length=225)


class Case(models.Model):
    name = models.CharField(max_length=225)
    owner = models.ForeignKey(UserModel, null=True,
                              on_delete=models.DO_NOTHING)


class Person(models.Model):
    name = models.CharField(max_length=225)
    cases = models.ManyToManyField('Case')
    teams = models.ManyToManyField(Team)
