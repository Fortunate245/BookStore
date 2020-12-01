from django.db import models
from django.utils import timezone

class Book(models.Model):
	name = models.CharField(max_length=40,null = False)
	author = models.CharField(max_length=50,null=False)
	isbn = models.BigIntegerField(unique=True,null = False)
	book_url = models.URLField(default='https://www.bookcamp.com')
	pub_date = models.DateTimeField('date published',default=timezone.now)


	def __str__(self):
		return f"{self.name} Book"