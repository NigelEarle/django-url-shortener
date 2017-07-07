import random
from django.db import models

# Create your models here.

def code_generator(size=6, chars='abcdefghijklmnopqrstuvwxyz'):
  # new_code = ''
  # for _ in range(chars):
  #   new_code += random.choice(chars)
  # return new_code
  return ''.join(random.choice(chars) for _ in range(size))

class KirrURL(models.Model):
  url = models.CharField(max_length=220, )
  shortcode = models.CharField(max_length=15, unique=True)
  updated = models.DateTimeField(auto_now=True)
  timestamp = models.DateTimeField(auto_now_add=True)

  def save(self, *args, **kwargs):
    print("something")
    self.shortcode = code_generator()
    super(KirrURL, self).save(*args, **kwargs)


  def __str__(self):
    return str(self.url)