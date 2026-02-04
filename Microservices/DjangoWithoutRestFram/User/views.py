from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from .models import User
import json

def login_view(request):
    if request.method == "POST":    
        email = request.POST.get("email")
        password = request.POST.get("password")

        # Here django only checks whether user with the given email exist or not. if yes then it matches the password with what stored in db and returns an user object
        user = authenticate(request, email=email, password=password) 
        print(user)

        if user:
            #Here django actually creates a session (key-value pair){session-key: session-id} and stores in db/cache(ref: django_sessions table) and it also sends this session values back to client/browser which browser stores at client side.
            login(request, user)
            return JsonResponse({"message": "Login successful"})
        return JsonResponse({"error": "Invalid credentials"}, status=400)


def logout_view(request):
    #Here first the sessionmiddleware intercepts this request and other request too, extracts the session data and matches with the stored data in db to check whether session is active or not and then attaches a session object in the request.session field. Further the Authentication middleware uses that session data, fetches the user object and attach that user to requesr.user which the logout method uses at the time of logout(see logout internal implementation). Further the logout also delets that session entry from db
    logout(request)
    return JsonResponse({"message": "Logged out"})

def register(request):
    if request.method == "POST":
        data = json.loads(request.body)

        email = data.get("email")
        password = data.get("password")
        username = data.get("username")

        if not email or not password:
            return JsonResponse({"error": "Email and password required"}, status=400)

        if User.objects.filter(email=email).exists():
            return JsonResponse({"error": "Email already exists"}, status=400)

        user = User.objects.create_user(
            email=email,
            password=password,
            username=username
        )

        return JsonResponse({"message": "User registered successfully"})