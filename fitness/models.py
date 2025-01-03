from django.db import models


# GOAL_PERIODS = (
#     ('7d', 'letzten  7 Tage'),
#     ('14d', 'letzten 14 Tage'),
#     ('30d', 'letzten 30 Tage'),
#     ('m', 'aktueller Monat'),
#     ('w', 'aktuelle Woche'),
# )


class Workout(models.Model):
    date = models.DateTimeField(verbose_name="Datum")
    name = models.CharField(verbose_name="Name", max_length=255)
    url = models.URLField(verbose_name="URL", null=True, blank=True)
    app = models.TextField(verbose_name="App", null=True, blank=True)
    notes = models.CharField(max_length=255, null=True, blank=True)

    distance = models.DecimalField(verbose_name="Distanz", max_digits=4, decimal_places=2, null=True, blank=True)
    duration = models.DurationField(verbose_name="Dauer", null=True, blank=True)

    date_created = models.DateTimeField(auto_now_add=True, verbose_name="Datum d. Erstellung")

    discipline = models.ForeignKey('Discipline', models.PROTECT)
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


class Discipline(models.Model):
    name = models.CharField(verbose_name="Name", max_length=255)

    class Meta:
        ordering = ["name"]
        verbose_name_plural = "Sportart"
        verbose_name = "Sportart"

    def __str__(self):
        return self.name

# class Goal(models.Model):
#     date_created = models.DateField(auto_now_add=True)
#
#     # Selection by time
#     period = models.CharField(max_length=20, choices=GOAL_PERIODS, verbose_name="Zeitraum")
#
#     # Selection by property
#     name = models.CharField(max_length=255, null=True, blank=True)
#     discipline = models.ForeignKey('Discipline', models.PROTECT, null=True, blank=True, verbose_name="Disziplin")
#     condition = models.ForeignKey('Condition', models.PROTECT, null=True, blank=True, verbose_name="Kondition")
#     muscle_group = models.ForeignKey('MuscleGroup', models.PROTECT, null=True, blank=True, verbose_name="Muskelgruppe")
#
#     # Count
#     count = models.PositiveSmallIntegerField(verbose_name="Anzahl an Workouts")
#
#     class Meta:
#         ordering = ["condition"]
#         verbose_name = "Ziel"
#         verbose_name_plural = "Ziele"
#
#     def clean(self):
#         if not self.condition and not self.muscle_group and not self.name and not self.discipline:
#             raise ValidationError('Kondition, Musklegruppe, Disziplin oder Name muss angegeben sein')
#         if self.name and (self.muscle_group or self.condition or self.discipline):
#             raise ValidationError('Wenn Name angegeben ist, darf keine Muskelgruppe oder Kondition angegeben sein')
#
#     def _get_conditions(self):
#         conditions = []
#         if self.condition:
#             conditions.append(str(self.condition))
#         if self.muscle_group:
#             conditions.append(str(self.muscle_group))
#         if self.name:
#             conditions.append(self.name)
#         return conditions
#
#     def __str__(self):
#         return f"{', '.join(self._get_conditions())}: {self.count} {self.get_period_display()}"
#
#     def select_matching_workouts(self):
#         """
#         Get number of days satisfying the condition"
#         """
#         today = datetime.now().date()
#
#         params = dict()
#         if self.period == "w":
#             week_start = today - timedelta(days=today.weekday())
#             week_end = week_start + timedelta(days=6)
#             params = dict(
#                 date__gte=week_start,
#                 date__lte=week_end,
#             )
#         elif self.period == "m":
#             _, num_days = monthrange(today.year, today.month)
#             month_start = datetime(today.year, today.month, 1)
#             month_end = datetime(today.year, today.month, num_days)
#             params = dict(
#                 date__gte=month_start,
#                 date__lte=month_end,
#             )
#         elif self.period == "7d":
#             params = dict(
#                 date__gte=today - timedelta(days=7),
#                 date__lte=today,
#             )
#         elif self.period == "14d":
#             params = dict(
#                 date__gte=today - timedelta(days=14),
#                 date__lte=today,
#             )
#         elif self.period == "30d":
#             params = dict(
#                 date__gte=today - timedelta(days=30),
#                 date__lte=today,
#             )
#
#         # Filter workouts
#         workouts = Workout.objects.filter(**params)
#         if self.condition:
#             workouts = workouts.filter(conditions=self.condition)
#         if self.muscle_group:
#             workouts = workouts.filter(muscle_groups=self.muscle_group)
#         if self.name:
#             workouts = workouts.filter(name=self.name)
#
#         return workouts
#
#     def is_satisfied(self):
#         return self.select_matching_workouts().count() >= self.count
#
#     def is_almost_satisfied(self):
#         return self.select_matching_workouts().count() > 0 and self.select_matching_workouts().count() + 1 == self.count
