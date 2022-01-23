from django.db import models

# Create your models here.
class MailModel(models.Model):
	company_name 	= models.CharField(max_length=100)
	company_email 	= models.EmailField()
	name 			= models.CharField(max_length=100)
	email 			= models.EmailField()
	message 		= models.CharField(max_length=700)

	class Meta:
		verbose_name_plural = "Mails"

	def __str__(self):
		return self.name 