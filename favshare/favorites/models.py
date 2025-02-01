# models.py
from django.db import models
from django.contrib.auth.models import User

class FavoriteItem(models.Model):
    TYPE_CHOICES = [
        ('MOVIE', 'Movie'),
        ('BOOK', 'Book'),
        ('SERIES', 'Web Series'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.get_type_display()}: {self.title}"
