from django.http import HttpResponse
from .models import Client
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ClientSerializer


@api_view(['POST'])
def create_client(request):
    client_data = ClientSerializer(data=request.data)
    if client_data.is_valid():
        client_data.save()
        return Response({"data": "Create user - success"})
    else:
        return HttpResponse(status=400)


@api_view(['GET'])
def read(request):
    try:
        data = Client.objects.values()
        return Response({"data": data})
    except Exception:
        return HttpResponse(status=204)


@api_view(['GET'])
def details_client_view(request, id):
    try:
        client_data = Client.objects.values().get(id=id)
        return Response({"data": client_data})
    except Exception:
        return HttpResponse(status=204)



@api_view(['POST'])
def delete_client(request, id):
    try:
        data = Client.objects.get(id=id)
    except Exception:
        return HttpResponse(status=204)
    if request.method == 'POST':
        data.delete()
        return Response({"data": "Client was deleted"})
    else:
        return Response({"data": "Client was not deleted"})


@api_view(['POST', 'GET'])
def update_client_details(request, id):
    try:
        if request.method == "POST":
            client = Client.objects.get(id=id)
            client.last_name = request.data.get("last_name")
            client.name = request.data.get("name")
            client.middle_name = request.data.get("middle_name")
            client.phone_number = request.data.get("phone_number")
            client.address = request.data.get("address")
            client.rate = request.data.get("rate")
            client.save()
            return Response({"data": "Client data was updated"})
        else:
            client = Client.objects.values().get(id=id)
            return Response({"data": client})
    except Exception:
        return HttpResponse(status=204)
