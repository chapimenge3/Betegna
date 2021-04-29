# Python Builtin import
import uuid

# Django Import 
from django.core.validators import RegexValidator


def user_directory_path(instance, filename):
    ext = (filename).split(".")[-1]
    filename = str(uuid.uuid1())
    print(instance)
    return f"users/{instance.id}{filename}.{ext}"


PHONE_REGEX = RegexValidator(
        regex=r'^\+?1?\d{10,15}$',
        message='Phone number must be entered in the format : 09******** or +2519******** up to 15 digits allowed',
        )