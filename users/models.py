from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# One-to-one relationship with the existing user model
class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	image = models.ImageField(default='default-user.png', upload_to='profile_pics')

	def __str__(self):
		return f'{self.user.username} Profile'



			
			
			
			
			
