from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
from django.core.mail import send_mail
from django.conf import settings
from django.utils.translation import gettext_lazy as _
import os
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import IntegrityError


# Custom User Manager
class CustomUserManager(UserManager):
    """Custom user manager for the user model"""

    def create_user_account_and_send_mail(self, student_id=None, email=None):
        """This method will take a student ID, email, campus and create an account. Then email the credentials to the email"""
        # generate password
        password = self.make_random_password(length=8)
        # create user account
        try:
            self.create_user(username=student_id, email=email, password=password)
            print(f"----------------- Account created for {student_id} -------------------")
        except IntegrityError as e:
            print(f"Error {e} occurred")
        except ValueError as e:
            print(f"Error {e} occurred")
        else:
            # send email
            subject = "Credentials to vote in the ASA Elections 2021"
            message = f"PLEASE USE THIS TO LOG IN\n\nStudent ID: {student_id}\nPassword: {password}\n\nUse it to login so that you can vote."
            send_mail(
                subject=subject,
                message=message, 
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[email],
                fail_silently=False,
            )
            # Get user and mark user as credentials_sent
            user = get_user_model().objects.get(username=student_id)
            user.credentials_sent = True
            user.save()
            print(f"----------------- Email for {student_id} account sent to {email} successfully --------------------")



class User(AbstractUser):
    """Model to represent a user"""

    voted = models.BooleanField(default=False)

    objects = CustomUserManager()

    def __str__(self):
        return self.username


class CreateAccountAndMailStudent(models.Model):
    batch = models.CharField(
        _("Name of Batch"),
        max_length=100,
        help_text="Enter name of batch you are uploading. eg. First Batch",
        null=False,
        blank=False)
    csv = models.FileField(
        _("CSV File"),
        help_text="Upload the CSV file to create the accounts",
        upload_to="accounts/csv/",
        null=False,
        blank=False)

    def __str__(self):
        return self.batch

    def clean(self):
        extension = os.path.splitext(self.csv.url)[1]
        print(extension)
        if extension != ".csv":
            raise ValidationError(_("The file is supposed to be a csv file"))

    class Meta:
        verbose_name = "Create Account and Mail Student"
        verbose_name_plural = "Create Account and Mail Student"


@receiver(post_save, sender=CreateAccountAndMailStudent)
def create_accounts(sender, instance, **kwargs):
    get_user_model().objects.auto_create_users(f"{instance.csv.url}")
    # if not settings.DEBUG:
        
    # get_user_model().objects.auto_create_users(f"data/{instance.csv.url}")