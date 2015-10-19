from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class CarModel(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name


class CarMark(models.Model):
    name = models.CharField(max_length=32)
    model = models.ForeignKey(CarModel)

    def __str__(self):
        return '{} {}'.format(self.model, self.name)


class Car(models.Model):
    year = models.PositiveSmallIntegerField(validators=[MinValueValidator(1900), MaxValueValidator(2100)])
    mark = models.ForeignKey(CarMark)

    def __str__(self):
        return '{} ({})'.format(self.mark, self.year)
