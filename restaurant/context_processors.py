from restaurant.models import Subscribe


def total_view(request):
    myvalue = request.POST.get("subscribe")
    print(myvalue)
    if myvalue:
        obj = Subscribe(phone_number=myvalue)
        obj.save()
    return None
