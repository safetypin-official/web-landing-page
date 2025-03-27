import uuid
from django.shortcuts import render
from django.http import HttpResponseBadRequest, JsonResponse
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

def open_post(request, post_id):
    try:
        # Parse post_id as a UUID
        post_id = uuid.UUID(post_id)
    except ValueError:
        # Return a 400 Bad Request response if post_id is not a valid UUID
        return HttpResponseBadRequest("Invalid post ID format")
    # receive param "post_id" from request and pass the value to html with context 
    return render(request, "OpenPost.html", {"post_id": post_id})