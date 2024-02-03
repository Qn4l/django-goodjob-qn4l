import uuid

from django.db import models
from django.utils.text import slugify


# Create your models here.


class Skill(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return f"Skills: {self.name}"


class Author(models.Model):
    name = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    designation = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.name} - {self.company}"


class Location(models.Model):
    country = models.CharField(max_length=200, verbose_name='Country')
    city = models.CharField(max_length=200, verbose_name='City')
    state = models.CharField(max_length=200, verbose_name='State')
    zipcode = models.CharField(max_length=200, verbose_name='Zipcode')

    def __str__(self):
        return f"(Location: {self.country}, {self.city})"


class JobPost(models.Model):
    job_type_choices = [
        ('Full Time', 'Full Time'),
        ('Part Time', 'Part Time'),
    ]
    objects = None
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=200, verbose_name='Title')
    description = models.TextField(verbose_name='Description')
    salary = models.FloatField(verbose_name='Salary')
    date_posted = models.DateTimeField(auto_now_add=True, verbose_name='Date Posted')
    slug = models.SlugField(null=True, unique=True, verbose_name='Slug', max_length=40)
    expiry_date = models.DateField(null=True, verbose_name='Expiry Date')
    location = models.OneToOneField(Location, on_delete=models.CASCADE, verbose_name='Location',
                                    blank=True, null=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, verbose_name='Author', blank=True, null=True)
    skills = models.ManyToManyField(Skill, verbose_name='Skills', blank=True)
    type = models.CharField(max_length=200, verbose_name='job_type', null=False,
                            choices=job_type_choices)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super(JobPost, self).save(*args, **kwargs)

    def __str__(self):
        return f"({self.title}, Salary: {self.salary})"
