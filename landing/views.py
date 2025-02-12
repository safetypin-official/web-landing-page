from django.shortcuts import render
from django.http import JsonResponse
from .models import Subscriber

from django_user_agents.utils import get_user_agent

def home(request):
    user_agent = get_user_agent(request)
    
    if user_agent.is_mobile:
        template = "mobile/index.html"
    elif user_agent.is_tablet:
        template = "desktop/index.html"
    else:
        template = "desktop/index.html"

    return render(request, template)

def subscribe(request):
    if request.method == "POST":
        email = request.POST.get("email") 
        print("yikes")
        if not email:
            return JsonResponse({"error": "Email is required"}, status=400)

        # Check if email already exists
        if Subscriber.objects.filter(email=email).exists():
            return JsonResponse({"error": "Email is already subscribed"}, status=400)

        # Save email to database
        subscriber = Subscriber(email=email)
        subscriber.save()

        return JsonResponse({"success": "Subscription successful"}, status=200)

    return JsonResponse({"error": "Invalid request"}, status=400)