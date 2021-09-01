from django.db import models
import string
import random

def generate_unique_code():
    length = 8

    while True:
        code = ''.join(random.choices(string.ascii_uppercase, k=length))
        if Kennel.objects.filter(code=code).count() == 0:
            break
    return code
# Create your models here.

class Kennel(models.Model):
    code = models.CharField(max_length=8, default="", unique=True)
    manager = models.CharField(max_length=50, unique=True)
    guest_can_pause = models.BooleanField(null=False, default=False)
    guest_can_skip = models.BooleanField(null=False, default=1)
    created_at = models.DateTimeField(auto_now_add=True)

    