from pyexpat import model
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class Review(models.Model):
    user_name = models.CharField(max_length=20)
    review_text = models.TextField()
    rating = models.IntegerField(validators=[MinValueValidator, MaxValueValidator])

    def __str__(self) -> str:
        return f"{self.user_name} msg:'{self.review_text[:20]}' rating:{self.rating}"