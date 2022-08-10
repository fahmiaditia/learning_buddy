from django.db import models

# Create your models here.
class News(models.Model):
	title = models.CharField(max_length=120, null=True, blank=True)
	text = models.TextField(null=True, blank=True)

	def __str__(self):
		return f"{self.title}"