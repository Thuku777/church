from django.db import models

# Create your models here.
class ChurchContact(models.Model):
    church_phone = models.CharField(max_length=100)
    church_email = models.CharField(max_length=100)
    church_location = models.CharField(max_length=100)

    class Meta:
            verbose_name = 'CHurch Contact'
            verbose_name_plural = 'Church Contancts'
            ordering = ['-id']
    
    def __str__(self):
        return self.church_email

