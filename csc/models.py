from django.db import models

class user(models.Model):
    steam64 = models.CharField(max_length=17)
    def __str__(self):
        return self.steam64


class lastSession(models.Model):
    userID = models.ForeignKey(user)
    date = models.DateTimeField('timestamp')
    name = models.CharField(max_length=200)
    value = models.IntegerField(default=0)
    def __str__(self):
        return self.name


class accuracy(models.Model):
    userID = models.ForeignKey(user)
    date = models.DateTimeField('timestamp')
    weapon_type = models.CharField(max_length=200)
    weapon_accuracy = models.IntegerField(default=0)
    def __str__(self):
        return self.weapon_type