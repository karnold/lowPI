from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from air import suspension
import time

@api_view(['POST'])

def rideControl(request):
    s = suspension.suspension()

    switch = request.DATA.get('switch')

    getattr(s, switch)()

    response = Response('ok')
    response['Cache-Control'] = 'no-cache'
    return response 
