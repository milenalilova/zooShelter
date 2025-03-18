from django.db import models
from django.utils.text import slugify


class AnimalCategory(models.Model):
    name = models.CharField(
        max_length=100
    )
    description = models.TextField(
        blank=True,
        null=True
    )
    slug = models.SlugField(
        unique=True,
        blank=True
    )

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Animal Categories'


class Animal(models.Model):
    class StatusChoices(models.TextChoices):
        AVAILABLE = 'Available', 'Available'
        IN_TREATMENT = 'In Treatment', 'In Treatment'
        RECOVERING = 'Recovering', 'Recovering'

    personal_name = models.CharField(
        max_length=100
    )
    common_name = models.CharField(
        max_length=100
    )
    species = models.CharField(
        max_length=100
    )
    gender = models.CharField(
        max_length=50
    )
    age_estimate = models.CharField(
        max_length=50,
        blank=True,
        null=True
    )
    description = models.TextField()
    rescue_date = models.DateField()

    status = models.CharField(
        max_length=20,
        choices=StatusChoices,
        default=StatusChoices.AVAILABLE
    )
    additional_info = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )
    slug = models.SlugField(
        unique=True,
        blank=True
    )

    category = models.ForeignKey(
        AnimalCategory,
        on_delete=models.PROTECT,
        related_name='animals'
    )

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f"{self.common_name}-{self.pk}")
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.personal_name} ({self.species})"


#     TODO get_absolute_url

class AnimalImage(models.Model):
    image = models.ImageField(
        upload_to='animals/'
    )
    is_primary = models.BooleanField(
        default=False
    )
    caption = models.CharField(
        max_length=200,
        blank=True,
        null=True
    )

    animal = models.ForeignKey(
        Animal,
        on_delete=models.CASCADE,
        related_name='images'
    )

    def __str__(self):
        return f"Image for {self.animal.personal_name}"
