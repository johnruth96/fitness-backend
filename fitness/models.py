from django.db import models


class Activity(models.Model):
    name = models.CharField(verbose_name="Name", max_length=255)

    class Meta:
        ordering = ["name"]
        verbose_name_plural = "Sportart"
        verbose_name = "Sportart"

    def __str__(self):
        return self.name


class MuscleGroup(models.Model):
    name = models.CharField(verbose_name="Name", max_length=255)

    class Meta:
        ordering = ["name"]
        verbose_name_plural = "Muskelgruppen"
        verbose_name = "Muskelgruppe"

    def __str__(self):
        return self.name


class Condition(models.Model):
    name = models.CharField(verbose_name="Name", max_length=255)

    class Meta:
        ordering = ["name"]
        verbose_name_plural = "Sportliche Konditionen"
        verbose_name = "Sportliche Kondition"

    def __str__(self):
        return self.name


class Workout(models.Model):
    activity = models.ForeignKey('Activity', models.PROTECT)
    date_created = models.DateTimeField(auto_now_add=True, verbose_name="Datum d. Erstellung")

    date = models.DateTimeField(verbose_name="Datum")
    name = models.CharField(verbose_name="Name", max_length=255, blank=True, null=True)
    url = models.URLField(verbose_name="URL", null=True, blank=True)
    app = models.TextField(verbose_name="App", null=True, blank=True)
    notes = models.CharField(max_length=255, null=True, blank=True)

    distance = models.DecimalField(verbose_name="Distanz", max_digits=4, decimal_places=2, null=True, blank=True)
    duration = models.DurationField(verbose_name="Dauer", null=True, blank=True)

    conditions = models.ManyToManyField('Condition', verbose_name="Sportliche Kondition", blank=True)
    muscle_groups = models.ManyToManyField('MuscleGroup', verbose_name="Muskelgruppe", blank=True)

    class Meta:
        ordering = ["-date", "name"]

    def __str__(self):
        return self.name

    @property
    def pace(self):
        if self.distance and self.duration:
            return self.duration / float(self.distance)
        return None
