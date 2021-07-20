from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
from django.core.mail import send_mail
import csv
from django.conf import settings


# Custom User Manager
class CustomUserManager(UserManager):
    """Custom user manager for the user model"""

    def auto_create_users(self, csv_file):
        """Create users from a csv file, using the student ID column as the the username, auto generate password for the account and email the credentials to the email associated with the student ID"""

        # read the data from the csv file
        # for each data in the csv, read the first item as the Student ID and the second as the email
        # Create a user account using the Student ID as the username
        # Email the Student ID and the Password to the email

        if csv_file is None:
            raise ValueError("A csv file is required")  
        
        # open the csv file
        with open(csv_file, "r") as file:
            my_data_reader = csv.reader(file, delimiter=",")
            students_data = [data for data in my_data_reader][1:]

            # Create accounts and send mail
            for student_data in students_data:
                student_id = student_data[0]
                email = student_data[1]
                password = self.make_random_password(length=8)
                self.create_user(student_id, email, password)

                message = f"Student ID: {student_id} -- Password: {password}"
                send_mail(
                    "Credentials for voting",
                    message,
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=[email],
                    fail_silently=False
                )
                print("----------------- Credentials Sent ----------------")

class User(AbstractUser):
    """Model to represent a user"""
    
    voted = models.BooleanField(default=False)

    objects = CustomUserManager()

    def __str__(self):
        return self.username


# TODO - use the student id to log the students in
# TODO - generate random password to each student that will be emailed to them