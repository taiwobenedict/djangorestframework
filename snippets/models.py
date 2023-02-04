from django.db import models


# Create your models here.
COUNTRY = [
  ('DEFAULT', '-----'),
  ('FRC','France'),
  ('JPA','Japan'),
  ('NGA','Nigeria'),
  ('USA','USA'),
]

GENDER = [
  ('DEFAULT', '-----'),
  ('M', 'Male'),
  ('F', 'Female'),
]

# Snippets  Moodel

class Author(models.Model):
  name = models.CharField(max_length=150, default='') 
  gender = models.CharField(max_length=50, choices=GENDER, default='DEFAULT')
  country = models.CharField(max_length=50, choices=COUNTRY, default="DEFAULT")

  def __str__(self):
      return self.name
  
class Snippet(models.Model):
  created = models.DateTimeField(auto_now_add=True)
  title = models.CharField(max_length=50, default='')
  code = models.TextField()
  language = models.CharField(max_length=50)
  owner = models.ForeignKey("auth.User", on_delete=models.CASCADE, related_name="snippets")

  def __str__(self):
      return self.title
  
