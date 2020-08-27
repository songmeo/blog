from django.db import models
from django.db.models import (
    CharField,
    DateField,
    ManyToManyField,
    Model,
    SlugField,
    TextField,
)
# Create your models here.
class Tag(Model):
    name = CharField(
        max_length=31,
        unique=True,
    )
    slug = SlugField(
        max_length=31,
        unique=True,
        help_text="A label for URL config.")
    class Meta:
        ordering = ["name"]

class Startup(Model):
    name = CharField(
        max_length=31,
        db_index=True,
    )
    slug = SlugField(
        max_length=31,
        unique=True,
        help_text="A label for URL config."
    )
    description = TextField()
    founded_date = DateField("date founded")
    contact = EmailField()
    website = URLField(max_length=255)
    tags = ManyToManyField(Tag)
    
    class Meta:
        get_latest_by = "founded_date"
        ordering = ["name"]

    def __str__(self):
        return self.name

class NewsLink(Model):
    name = CharField(max_length=31)
    slug = SlugField(max_length=31)
    pub_date = DateField("date published")
    link = URLField(max_length=255)
    startup = ForeignKey(Startup, on_delete=models.CASCADE)
    class Meta:
        get_latest_by = "pub_date"
        ordering = ["-pub_date"]
        unique_together = ("slug", "startup")
        verbose_name = "news article"

    def __str__(self):
        return f"{self.startup}: {self.title}"

