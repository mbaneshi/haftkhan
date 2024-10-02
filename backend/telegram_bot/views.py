from django.shortcuts import render

# Create your views here.
# telegram_bot/views.py

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import requests

@csrf_exempt  # Disable CSRF for this view
def webhook(request):
    if request.method == 'POST':
        update = json.loads(request.body)
        # Handle the update here (e.g., process messages)
        chat_id = update['message']['chat']['id']
        text = update['message']['text']
        
        # Example: reply back to the user
        reply_text = f"You said: {text}"
        send_message(chat_id, reply_text)
        
        return JsonResponse({"status": "ok"})
    return JsonResponse({"status": "invalid method"}, status=405)

def send_message(chat_id, text):
    token = '7188599444:AAF2mowmsgeADWadlyaN_wTTZcSP17AhZA0'
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {
        'chat_id': chat_id,
        'text': text
    }
    requests.post(url, json=payload)

