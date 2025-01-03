from django.contrib import admin

from fitness.models import Workout, MuscleGroup, Condition, Discipline


class WorkoutAdmin(admin.ModelAdmin):
    list_display = ('name', 'date')


# class GoalAdmin(admin.ModelAdmin):
#     list_display = ('condition', 'muscle_group', 'name', 'count', 'period')


admin.site.register(Workout, WorkoutAdmin)
# admin.site.register(Goal, GoalAdmin)
admin.site.register(Condition)
admin.site.register(MuscleGroup)
admin.site.register(Discipline)
