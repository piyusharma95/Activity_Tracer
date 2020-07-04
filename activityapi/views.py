from datetime import datetime
import json

from django.http import HttpResponse
from django.contrib.auth.models import User

from .serializers import MemberSerializer
from .models import Member, ActivityPeriod


def member_activies(request):
    json_response = {}
    json_response["ok"] = "true"
    members = []
    for i in Member.objects.all():
        member_json = {}
        temp_ser = MemberSerializer(instance=i).data
        member_json["id"] = temp_ser['user']
        user = User.objects.get(pk=temp_ser['user'])
        member_json["real_name"] = user.first_name + " " + user.last_name
        member_json["tz"] = str(temp_ser['tz'])
        activity_list = []
        for j in temp_ser['activity']:
            activity_instance = list(j.items())
            activity_json = {}
            activity_json["start_time"] = datetime.strptime(activity_instance[0][1], '%Y-%m-%dT%H:%M:%S.%fZ').strftime('%b %d %Y %H:%M%p')
            activity_json["end_time"] = datetime.strptime(activity_instance[1][1], '%Y-%m-%dT%H:%M:%S.%fZ').strftime('%b %d %Y %H:%M%p')
            activity_list.append(activity_json)
        member_json["activity_periods"] = activity_list
        members.append(member_json)
    json_response["members"] = members
    json_pretty = json.dumps(json_response, indent=4)
    return HttpResponse(json_pretty, content_type="application/json")