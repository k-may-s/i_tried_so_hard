from django.http import Http404
from django.shortcuts import get_object_or_404, redirect
from .models import Client
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ClientSerializer


@api_view(['POST'])
def create_client(request):
    client_data = ClientSerializer(data=request.data)
    if client_data.is_valid():
        client_data.save()
        return Response({"response": "Create user - success"})
    else:
        return Response({'response': "Something wrong... Again..."})


@api_view(['GET'])
def read(request):
    data = Client.objects.values()
    return Response({"data": data})


@api_view(['GET'])
def details_client_view(request, id):
    try:
        client_data = Client.objects.values().get(id=id)
    except Exception:
        raise Http404('Client not found')
    return Response({"data": client_data})


@api_view(['POST'])
def delete_client(request, id):
    try:
        data = get_object_or_404(Client, id=id)
    except Exception:
        raise Http404('Client not found')
    if request.method == 'POST':
        data.delete()
        return Response({"data": "Client was deleted"})
    else:
        return Response({"data": "Client was not deleted"})


@api_view(['GET', 'POST'])
def update_client_details(request, id):
    try:
        client = Client.objects.values().get(id=id)
        if request.method == "POST":
            client.last_name = request.POST.get("last_name")
            client.name = request.POST.get("name")
            client.middle_name = request.POST.get("middle_name")
            client.phone_number = request.POST.get("phone_number")
            client.address = request.POST.get("address")
            client.rate = request.POST.get("rate")
            client.save()
            return redirect("<int:id>/")
        else:
            return Response({"data": client})
    except Exception:
        raise Http404('Client not found')
