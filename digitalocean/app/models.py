from django.db import models


class UrlsDone(models.Model):
    url = models.CharField(max_length=2000)

    def __str__(self):
        return self.url


class UrlsLeft(models.Model):
    url = models.CharField(max_length=2000)

    def __str__(self):
        return self.url


class UrlsSaved(models.Model):
    url = models.CharField(max_length=2000)

    def __str__(self):
        return self.url
