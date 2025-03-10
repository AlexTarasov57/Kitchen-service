from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from django.utils import timezone


class DishType(models.Model):
    name = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField(default=timezone.now, editable=False)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Cook(AbstractUser):
    years_of_experience = models.IntegerField(default=0)

    class Meta:
        verbose_name = "сook"
        verbose_name_plural = "сooks"

    def __str__(self):
        return f"{self.username} ({self.first_name or ''} {self.last_name or ''})"

    # def get_absolute_url(self):
    #     return reverse("kitchen:cook-detail", kwargs={"pk": self.pk})


class Ingredient(models.Model):
    name = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField(default=timezone.now, editable=False)

    def __str__(self):
        return self.name


class Dish(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    dish_type = models.ForeignKey(DishType,on_delete=models.CASCADE)
    cooks = models.ManyToManyField(Cook, related_name="prepared_dishes")
    ingredients = models.ManyToManyField(Ingredient, related_name="used_in_dishes")
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now, editable=False)

    def __str__(self):
        return self.name
