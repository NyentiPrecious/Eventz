from django.shortcuts import render


def home(request):
        return render(request, 'home.html', {})
def event_list(request):
        return render(request, 'event_list.html', {})
# Create your views here.
