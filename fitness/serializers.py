from rest_framework import serializers

from fitness.models import Workout, Condition, MuscleGroup, Activity


class WorkoutSerializer(serializers.ModelSerializer):
    activity_str = serializers.StringRelatedField(source="activity")
    conditions_str = serializers.StringRelatedField(many=True, source="conditions", required=False)
    muscle_groups_str = serializers.StringRelatedField(many=True, source="muscle_groups", required=False)

    class Meta:
        model = Workout
        fields = '__all__'
        extra_kwargs = dict(
            date=dict(input_formats=["%d.%m.%Y, %H:%M"]),
            activity=dict(required=True),
        )


class MuscleGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = MuscleGroup
        fields = '__all__'


class ConditionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Condition
        fields = '__all__'


class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = '__all__'
