from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
	title = models.CharField(max_length=255)
	url = models.URLField()
	pub_date = models.DateTimeField(auto_now=False)
	votes_total = models.IntegerField(default = 1)
	image = models.ImageField(upload_to='images/')
	icon = models.ImageField(upload_to='icon_images/')
	body = models.TextField()
	hunter = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.title

	def summary(self):
		return self.body[:300]

	def pub_date_pretty(self):
		return self.pub_date.strftime('%b %e %Y')