from rest_framework import serializers

from .models import Member, ActivityPeriod


class AcivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = ActivityPeriod
        fields = ['start_time', 'end_time']


class MemberSerializer(serializers.ModelSerializer):
    activity = AcivitySerializer(many=True, read_only=True)

    class Meta:
        model = Member
        fields = ['user', 'tz', 'activity']
