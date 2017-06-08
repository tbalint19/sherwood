from django.db import models

class Story(models.Model):
    ANNOUNCEMENT = "Announcement"
    NEWS = "News"
    MATCH = "Match"
    PREVIEW = "Preview"
    content_type_choices = ((ANNOUNCEMENT, "Announcement"), (NEWS, "News"), (MATCH, "Match"), (PREVIEW, "Preview"))

    content_type = models.CharField(max_length=12, choices=content_type_choices, default=ANNOUNCEMENT)
    text = models.CharField(max_length=150)
    link = models.CharField(max_length=150)
    created = models.DateTimeField()

class Advert(models.Model):

    text = models.CharField(max_length=150)
