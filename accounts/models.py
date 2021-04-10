from django.contrib.auth.models import User
from django.db.models import *


class Profile(Model):
    user = OneToOneField(User, on_delete=CASCADE)

    def __str__(self):
        return self.user
