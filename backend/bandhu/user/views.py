from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
import json
from django.contrib.auth import authenticate, login, logout


# Create your views here.

@csrf_exempt
def signup(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            username = data.get("username")
            email = data.get("email")
            password = data.get("password")
            
            if not username or not password:
                return JsonResponse({"error": "Username and password are required."}, status=400)
            
            if User.objects.filter(email=email).exists():
                return JsonResponse({"error": "Email already exists."}, status=400)
            
            user = User.objects.create_user(username=username, email = email, password=password)
            
            return JsonResponse({"message": "User created successfully.", "user" : user})
        
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
