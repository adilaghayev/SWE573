from django.shortcuts import render


# Create your views here.
def home(request):

    return render(request, 'community_builder/home.html')


def about(request):
    return render(request, 'community_builder/about.html', {'title': 'About'})


