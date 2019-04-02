from django.db import models
from django.contrib.auth import models as auth_models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

# Create your models here.

UserModel = get_user_model()


class TeamPermission(models.Model):
    name = models.TextField()


class Group(models.Model):
    name = models.CharField(_('name'), max_length=80, unique=True)

    team = models.ForeignKey('Team', null=True, on_delete=models.DO_NOTHING)
    team_permissions = models.ManyToManyField(TeamPermission, blank=True)

    objects = auth_models.GroupManager()

    class Meta:
        verbose_name = _('group')
        verbose_name_plural = _('groups')

    def __str__(self):
        return self.name

    def natural_key(self):
        return (self.name,)


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
