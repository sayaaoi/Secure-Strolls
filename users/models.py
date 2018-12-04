from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# One-to-one relationship with the existing user model
class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	image = models.ImageField(default='default-user.png', upload_to='profile_pics')

	def __str__(self):
		return f'{self.user.username} Profile'


	def save(self):
		super().save()

		# resize the upload image
		img = Image.open(self.image.path)

		# check if image is more than 300 pixel
		if img.height > 300 or img.width > 300:
			output_size = (300, 300)
			img.thumbnail(output_size)
			img.save(self.image.path)

# Many-to-One relationship between saved routes and user model
# class SavedRoutes(models.Model):
# 	user = models.OneToOneField(User, on_delete=models.CASCADE)
# 	startLoc = models.
# 	endLoc = models.



