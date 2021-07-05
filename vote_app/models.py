from django.db import models
from django.utils.safestring import mark_safe
from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify
from django.conf import settings
from django.urls import reverse

User = settings.AUTH_USER_MODEL


class Category(models.Model):
    """Model to represent the categories the candidates are in"""
    name = models.CharField(_("Name of Category"),
                            max_length=50,
                            blank=False,
                            null=False,
                            help_text="Enter the name of the category")
    slug = models.SlugField(_("Slug"),
                            max_length=50,
                            blank=False,
                            null=False,
                            help_text="Slug of the category",
                            unique=True,
                            default="")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("vote_app:vote", kwargs={"slug": self.slug})

    def save(self, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(**kwargs)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class Candidate(models.Model):
    """Model to represent the candidate"""
    full_name = models.CharField(_("Name of Candidate"),
                                 max_length=50,
                                 blank=False,
                                 null=False,
                                 help_text="Enter the name of the candidate")
    picture = models.ImageField(_("Picture of Candidate"),
                                blank=False,
                                null=False,
                                upload_to="candidates/pictures/",
                                help_text="Upload the image of the candidate")
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="candidates",
        null=False,
        blank=False,
        help_text="Select the category the candidate belongs to")
    number_of_votes = models.PositiveIntegerField(_("Number of Votes"),
                                                  default=0)
    upvote = models.BooleanField(default=False)

    # display picture in admin
    def image_tag(self):
        if self.picture:
            return mark_safe(
                '<img src="%s" style="width: 100px; height:100px;" />' %
                self.picture.url)
        else:
            return 'No Image Found'

    image_tag.short_description = 'Image'

    def __str__(self):
        return self.full_name

    def save(self, **kwargs) -> None:
        if self.upvote is True:
            self.number_of_votes += 1
        return super().save(**kwargs)

    class Meta:
        verbose_name = "Candidate"
        verbose_name_plural = "Candidates"