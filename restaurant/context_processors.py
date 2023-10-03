from restaurant.models import Subscribe
from restaurant.models import MainDetails, SocialMedia

def total_view(request):
    myvalue = request.POST.get("subscribe")
    if myvalue:
        obj = Subscribe(phone_number=myvalue)
        obj.save()

    details = MainDetails.objects.first()
    socials = SocialMedia.objects.all()

    return {"details": details, "socials": socials}
