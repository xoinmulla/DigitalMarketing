from django.db import models
from django.contrib.auth.models import User

class Campaign(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Ad(models.Model):
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='ads/')  # Image upload
    link = models.URLField()
    views = models.PositiveIntegerField(default=0)
    clicks = models.PositiveIntegerField(default=0)

    def increment_views(self):
        self.views += 1
        self.save(update_fields=['views'])

    def increment_clicks(self):
        self.clicks += 1
        self.save(update_fields=['clicks'])

    def __str__(self):
        return self.title
