from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField("isim",max_length=255)
    subject = models.CharField("Konu başlığı", max_length=50)
    email = models.EmailField("E-mail")
    message = models.TextField("Mesaj", max_length=550)

    def __str__(self):
        return self.subject
    
    class Meta:
        verbose_name = "İletişim Formu Mesajı"
        verbose_name_plural = "İletişim Formu Mesajları"
