from django.shortcuts import render
from django.contrib.auth import authenticate, login as auth_login
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            auth_login(request, user)
            # Redirect to a success page.
            return JsonResponse({
              "status": True,
              "message": "Successfully Logged In!"
            })
        else:
            return JsonResponse({
              "status": False,
              "message": "Failed to Login, Account Disabled."
            })
            
    else:
        return JsonResponse({
          "status": False,
          "message": "Failed to Login, check your email/password."
        })