from django.db import models

# Create your models here.
category_choices = [('story', 'Story'), ('poem', 'Poem'), ('other', 'Other')]
catalog_choices = [('fiction', 'Fiction'), ('non-fiction', 'Non-fiction')]


class File(models.Model):
    file_name = models.CharField(max_length=100)
    description = models.TextField(default='')
    file = models.FileField(upload_to='files/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    is_malicious = models.BooleanField(default=True)
    category = models.CharField(max_length=20, choices=category_choices, default='other')
    catalog = models.CharField(max_length=20, choices=catalog_choices, default='non-fiction')
    author = models.CharField(max_length=100, default='Anonymous')

    def __str__(self):
        return self.file_name


class Cart(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    added_at = models.DateTimeField(auto_now_add=True)
    books = models.ManyToManyField(File)

    def __str__(self):
        return f"{self.user.username}'s cart"

