from django.db import models
from tinymce.models import HTMLField


# Create your models here.

class FAQ(models.Model):
    description = HTMLField()

    def __str__(self):
        return 'FAQ'

    class Meta:
        verbose_name = 'FAQ'
        verbose_name_plural = 'FAQs'


class FrequentlyAccordion(models.Model):
    faq = models.ForeignKey(FAQ, on_delete=models.CASCADE)
    title = models.CharField(max_length=2000)
    text = HTMLField()
