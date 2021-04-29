from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.utils.safestring import mark_safe
from django.core.validators import EmailValidator

#
from .utils import PHONE_REGEX, user_directory_path


class User(AbstractUser):
    '''
    User Model Inherited from AbstractUser and add custom field 
        - first name
        - last name
        - username 
        - email 
        - password
        - phone 
        - sex
        - profile picture
    '''

    email = models.EmailField(
        _('email address'), unique=True, validators=[EmailValidator])
    student_id = models.CharField(_("Student Id"), max_length=50, unique=True)
    phone = models.CharField(
        validators=[PHONE_REGEX], max_length=15, blank=True, null=True)
    sex = models.CharField(max_length=200, choices=(
        ('male', 'male'), ('female', 'female')))

    profile = models.ImageField(
        _("Image"),
        upload_to=user_directory_path,
        default="users/null.png",
        blank=True,
        null=True,
    )
    REQUIRED_FIELDS = [
        'first_name', 'email', 'sex',
    ]

    def image_tag(self):
        return mark_safe('<img src="%s" width="150" height="150"/>' % self.profile.url)

    image_tag.short_description = 'Photo'
    image_tag.allow_tags = True

    def __str__(self):
        return f"{self.username} : {self.first_name}"

    @property
    def get_full_name(self):
        """
        Return the first_name plus the last_name, with a space in between.
        """
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()
