from django.urls import path

from .views import health_check, emotion_response

urlpatterns = [
    path('', health_check.health_check),
    path('health_check/', health_check.health_check),
    path('emotion_check/', emotion_response.emotion_check),
    path('explain/', emotion_response.architecture_explain),
    path('chat/', emotion_response.chat_view, name='chat_view'),
    path('send-message/', emotion_response.send_message, name='send_message'),
]
