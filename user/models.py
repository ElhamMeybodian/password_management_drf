from django.db import models



class UserProfile(models.Model):
    username = models.CharField('username', max_length=50)

    def __str__(self):
        return self.username


class UserPassword(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='passwords')
    password = models.CharField('password', max_length=100)

    def __str__(self):
        return f'{self.password}--->{self.user}'
