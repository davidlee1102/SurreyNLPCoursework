from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def health_check(request):
    messsage = {
        'message': 'Health check successful'
    }
    return Response(messsage, status=status.HTTP_200_OK)