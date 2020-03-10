from django.db import models

# Create your models here.


class Series(models.Model):
    series_name = models.CharField(max_length=45)
    first_release_date = models.DateTimeField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return f"Series: {self.series_name}"


class PixarCharacter(models.Model):
    name = models.CharField(max_length=45)
    height = models.DecimalField(max_digits=4, decimal_places=2)
    description = models.TextField()
    series = models.ForeignKey(
        Series, related_name="characters_in_series", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return f"Name: {self.name}"
