from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.utils import timezone
from django import forms
from django.core import validators

def cannot_be_outdated(value):
    if value < timezone.now():
            raise forms.ValidationError('Datetime cannot be in the past')

# Create your models here.
class Song(models.Model):
    id = models.IntegerField(primary_key=True, unique=True)
    audio_file_type = models.CharField(max_length=100, blank=False, null=False, default="Song")
    song_name = models.CharField(max_length=100, blank=False, null=False)
    duration = models.IntegerField(blank=False, null=False)
    uploaded_date = models.DateTimeField(blank=False, null=False, validators=[cannot_be_outdated])

    def __str__(self):
        return self.song_name 

class Podcast(models.Model):
    id = models.IntegerField(primary_key=True, unique=True)
    audio_file_type = models.CharField(max_length=100, blank=False, null=False, default="Podcast") 
    podcast_name = models.CharField(max_length=100, blank=False, null=False)
    duration = models.IntegerField(blank=False, null=False)
    uploaded_date = models.DateTimeField(blank=False, null=False, validators=[cannot_be_outdated])
    host = models.CharField(max_length=100, blank=False, null=False)
    participants = ArrayField(models.CharField(max_length=100), size=10, blank=True)

    def __str__(self):
        return self.podcast_name

class Audiobook(models.Model):
    id = models.IntegerField(primary_key=True, unique=True)
    audio_file_type = models.CharField(max_length=100, blank=False, null=False, default="Audiobook") 
    title = models.CharField(max_length=100, blank=False, null=False)
    author = models.CharField(max_length=100, blank=False, null=False)
    narrator = models.CharField(max_length=100, blank=False, null=False)
    duration = models.IntegerField(blank=False, null=False)
    uploaded_date = models.DateTimeField(blank=False, null=False, validators=[cannot_be_outdated])

    def __str__(self):
        return self.title