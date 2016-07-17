from django.db import models
from django.utils.timezone import now


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/%Y/%m/%d', blank=True)
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=False)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = now()
        self.save()

    def short_text(self):
        short = self.text[:150] + '...'
        return short

    def not_published(self):
        if not self.published_date:
            pass

    def __str__(self):
        return self.title
