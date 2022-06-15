from django.db import models
from django.contrib.auth.models import User

gender_choice = (
    ("male", "Male"),
    ("Female", "Female"),
    ("Third Gender", "Third Gender")
)


# Create your models here.
class ProfileModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='basic_user')
    age = models.PositiveIntegerField(blank=False)
    gender = models.CharField(choices=gender_choice, max_length=15)
    profile_picture = models.ImageField(upload_to='profile_images')
    join_date = models.DateField(auto_now=True)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name} {self.age}"