from django.shortcuts import render, redirect
from news.models import News, Images
from news.forms import NewsForm
from django.http import HttpResponse, JsonResponse
import uuid


# Create your views here.

def index_view(request):
    context = {}
    context["form"] = NewsForm()
    context["image_data"] = str(uuid.uuid4())
    if request.method == "POST":
        form = NewsForm(request.POST)
        if form.is_valid():
            news = form.save()
            image_data = request.POST.get("image_data")
            image_list = Images.objects.filter(image_token=image_data)
            if image_data:
                for image in image_list:
                    image.news = news
                    image.save()
            return redirect("home")
        else:
            context["form"] = form
    return render(request, "news-form.html", context)


def picture_add(request):
    if request.method == "POST":
        img = Images.objects.create(
            image=request.FILES.get("file"),
            image_token=request.POST.get("image_data")
        )
        return JsonResponse({
            "pk": img.id,
            "uploaded": True
        })
    else:
        return JsonResponse({
            "uploaded": False
        })


def picture_delete(request):
    if request.method == "POST":
        pk = request.POST.get("remove_object")
        img = Images.objects.filter(id=pk).last()
        if img:
            img.delete()
            return JsonResponse({
                "deleted": True
            })
        else:
            return JsonResponse({
                "deleted": False
            })
    else:
        return JsonResponse({
            "uploaded": False
        })
