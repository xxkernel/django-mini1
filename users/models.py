from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)  # Allow blank and null

    def __str__(self):
        return f'{self.user.username} Profile'

class Follow(models.Model):
    follower = models.ForeignKey(User, related_name="follower", on_delete=models.CASCADE)
    following = models.ForeignKey(User, related_name="following", on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.follower} follows {self.following}'

