from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request
from django.shortcuts import render
from django.http import JsonResponse

from HungLeCoursework.utils import emotion_model


@api_view(["POST"])
def emotion_check(request: Request):
    """Example
       {
           "sentence_data": "need not much very much real"
       }
       """
    data = request.data
    link_request = data.get("sentence_data", "")
    processed = emotion_model.emotion_predict(link_request)
    emotion_model.user_capture(link_request, processed)
    return Response(processed, status=status.HTTP_200_OK)


def architecture_explain(request):
    return render(request, 'index.html')


def chat_view(request):
    return render(request, 'chat.html')


def send_message(request):
    if request.method == 'POST':
        message = request.POST.get('message', '')
        if not message:
            return JsonResponse({'status': 'blank data, please check'})

        # Process the message here
        processed = emotion_model.emotion_predict(message)
        try:
            emotion_model.user_capture(message, processed)
        except Exception as E:
            print(E)
        response_data = {
            'message': message,
            'bot_response': processed,
            'status': 'success'
        }
        return JsonResponse(response_data)
    else:
        return JsonResponse({'status': 'error'})

