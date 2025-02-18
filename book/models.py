from django.db import models
from django.urls import reverse
from django.core.validators import MinValueValidator,MaxValueValidator

class Book(models.Model):
    GENRE_CHOISES=[
        ('fiction','Fiction'),
        ('non_fiction','Non_Fiction'),
        ('science','Science'),
        ('technology','Technology'),
        ('history','History'),
        ('other','Other'),
    ]

    title=models.CharField(max_length=200)
    author=models.CharField(max_length=200)
    description=models.TextField()
    genre=models.CharField(max_length=20,choices=GENRE_CHOISES)
    isbn=models.CharField('ISBN',max_length=13,unique=True)
    publication_date=models.DateField()
    avreage_rating=models.DecimalField(
        max_digits=3,
        decimal_places=2,
        validators=[MinValueValidator(0),MaxValueValidator(5)],default=0
    )
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    def get_absoute_url(self):
        return reverse('book-details',kwargs={'pk':self.pk})
    
