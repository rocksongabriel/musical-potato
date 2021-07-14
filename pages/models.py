from django.db import models
from django.utils.translation import gettext_lazy as _

class SupportForm(models.Model):
    full_name = models.CharField(_("Full Name"), max_length=50, help_text="Enter your full name", null=False, blank=False)
    student_id = models.CharField(_("Student ID"), max_length=20, help_text="Enter your ID", null=False, blank=False)
    email_address = models.EmailField(_("Email Address"), max_length=300, help_text="Enter your email address", blank=False, null=True)
    message = models.TextField(_("Complaint"), max_length=1000, help_text="Enter your message", null=False, blank=False)


    def __str__(self): 
        return f"{self.full_name}, {self.student_id}"

    class Meta:
        verbose_name = "Support Form"
        verbose_name_plural = "Support Forms"