from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .forms import GreetingForm


def greeting_view(request):
    if request.method == "POST":
        form = GreetingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("greeting_page", name=form.cleaned_data["name"])
    else:
        form = GreetingForm()

    return render(request, "greetings/greeting_form.html", {"form": form})


def greeting_page(request, name):
    return render(request, "greetings/greeting_page.html", {"name": name})
