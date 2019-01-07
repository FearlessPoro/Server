from django.http import HttpResponse, JsonResponse
from django.core import serializers
from django.template.loader import render_to_string
from django.views.decorators.csrf import csrf_exempt
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from Station_controls.functions import *
from Station_controls.models import AllMeasurements

def home(request):
    html = render_to_string('home.html')
    return HttpResponse(html)


class SendView(APIView):
    permission_classes = (IsAuthenticated,)

    @staticmethod
    @csrf_exempt
    def send(request):
        if request.method == 'POST':
            return_message = Functions.parse_send_request(request)
            return JsonResponse(return_message, safe=False)
        else:
            return_message = Constants.INCORRECT_REQUEST_TYPE_MESSAGE
        return HttpResponse(return_message, content_type="application/json")


def view_data_available(request):
    response_data = {"columns": [f.name for f in AllMeasurements._meta.get_fields()]}
    return JsonResponse(json.dumps(response_data), safe=False)

def view_stations_available(request):
    query = Stations.objects.all().only("Name")
    return_message = serializers.serialize("json", query)
    return JsonResponse(return_message, safe=False)

@csrf_exempt
def request_data(request):
    if request.method == 'POST':
        body_data = json.loads(request.body)
        print(body_data)
        query = AllMeasurements.objects.all()
        if "Time" in body_data:
            if body_data["Time"] == "day":
                query = query.filter(Czas_pomiaru__range=(datetime.today() - timedelta(days=1), datetime.today()))
            elif body_data["Time"] == "week":
                query = query.filter(Czas_pomiaru__range=(datetime.today() - timedelta(weeks=1), datetime.today()))
            elif body_data["Time"] == "month":
                query = query.filter(Czas_pomiaru__range=(datetime.today() - timedelta(days=30), datetime.today()))
            elif body_data["Time"] == "year":
                query = query.filter(Czas_pomiaru__range=(datetime.today() - timedelta(days=365), datetime.today()))
        if "Station" in body_data:
            query = query.filter(Stacja__exact=body_data["Station"])
        if "Column" in body_data:
            query = query.only(*body_data["Columns"])
        return_message = serializers.serialize("json", query)
        return JsonResponse(return_message, safe=False)

    else:
        return_message = Constants.INCORRECT_REQUEST_TYPE_MESSAGE
    return HttpResponse(return_message)







