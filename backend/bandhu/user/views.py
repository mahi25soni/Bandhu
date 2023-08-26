from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
import json
from django.contrib.auth import authenticate, login, logout
from .context import get_answer, chatbot
# from .category import start_conversation
from .models import Question, Sentiments
from .sentiment import get_sentiment


# Create your views here.

@csrf_exempt
def signup(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            print("nothign rey ", data)
            username = data.get('username')
            email = data.get('email')
            password = data.get('password')
            
            if not username or not password:
                return JsonResponse({"error": "Username and password are required."}, status=400)
            
            if User.objects.filter(email=email).exists():
                return JsonResponse({"error": "Email already exists."}, status=400)
            
            user = User.objects.create_user(username=username, email = email, password=password)
            
            return JsonResponse({"message": "User created successfully."})
        
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON data."}, status=400)
    else:
        return JsonResponse({"error": "Only POST requests are allowed."}, status=405)

@csrf_exempt
def login(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            username = data.get('username')
            password = data.get('password')
            
            if not username or not password:
                return JsonResponse({"error": "Username and password are required."}, status=400)
            
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                login(request, user)
                return JsonResponse({"message": "Login successful."})
            else:
                return JsonResponse({"error": "Invalid credentials."}, status=401)
            
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON data."}, status=400)
    else:
        return JsonResponse({"error": "Only POST requests are allowed."}, status=405)

@csrf_exempt
def question(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            question = data.get('question')
            answer = get_answer(chatbot, question)
            question = Question.objects.create(question = question)
            set_sentiment(question) 
            return HttpResponse(answer)
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON data."}, status=400)
    else:
        return JsonResponse({"error": "Only POST requests are allowed."}, status=405)
    

@csrf_exempt
def set_sentiment(question):
    try:
        senti_array = get_sentiment(question.question)
        for x in senti_array:
            for key, value in x.items():
                print("sent ", key, " percent ", value)
                sentiment = Sentiments.objects.create(question = question, name = key, percent = value)
    except:
        return JsonResponse({"error": "There's some error."}, status=400)