from rest_framework import serializers

from fitness.models import Workout, Condition, MuscleGroup, Discipline


class WorkoutSerializer(serializers.ModelSerializer):
    discipline_str = serializers.StringRelatedField(source="discipline")
    conditions_str = serializers.StringRelatedField(many=True, source="conditions", required=False)
    muscle_groups_str = serializers.StringRelatedField(many=True, source="muscle_groups", required=False)

    class Meta:
        model = Workout
        fields = '__all__'
        extra_kwargs = dict(
            date=dict(input_formats=["%d.%m.%Y, %H:%M"]),
            discipline=dict(required=True),
        )


class MuscleGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = MuscleGroup
        fields = '__all__'


class ConditionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Condition
        fields = '__all__'


class DisciplineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discipline
        fields = '__all__'

# class GoalSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Goal
#         fields = '__all__'
