from django.db import models

# Create your models here.
class Member(models.Model):
    name=models.CharField(max_length=255)
    description=models.TextField()
    def _str_(self):
        return self.name