'''
Model for Library application
'''
from django.db import models

# Create your models here.
class Book(models.Model):
    '''Model for Book entity'''
    title = models.CharField(max_length=250, null=False)
    author = models.CharField(max_length=100, null=False)
    isbn = models.CharField(max_length=13, null=False)
    description = models.TextField(max_length=300, null=True, blank=True)
    price = models.FloatField(max_length=5, null=False, default=1.0)

    def __str__(self) -> str:
        '''Return the title of the book'''
        return self.title
