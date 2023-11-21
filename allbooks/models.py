from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Collection(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='collection_images/', null=True, blank=True)
    description = models.TextField(default='')  # Set a default value
    source_url = models.URLField(blank=True, null=True)

    def get_absolute_url(self):
        return reverse('collection-detail', args=[str(self.id)])
    

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    genre = models.CharField(max_length=255)
    description = models.TextField()
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Chapter(models.Model):
    title = models.CharField(max_length=255)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Text(models.Model):
    content = models.TextField()
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE, related_name='text')
    
    def __str__(self):
        return f"Text {self.pk} of Chapter {self.chapter_id}"
    
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    reading_list = models.ManyToManyField(Book, related_name='reading_list', blank=True)
    group_readings = models.ManyToManyField(Book, related_name='group_readings', blank=True)
    
    def __str__(self):
        return self.user.username
    
    def add_book_to_reading_list(self, book):
      
        self.reading_list.add(book)
     

    def remove_book_from_reading_list(self, book):
        
        self.reading_list.remove(book)
        
    def add_book_to_group_readings(self, book):
       
        self.group_readings.add(book)  
        
    def remove_book_from_group_readings(self, book):
     
        self.group_readings.remove(book)      
 