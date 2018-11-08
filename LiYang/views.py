from django.shortcuts import render

from LiYang.models import House


def index(request):
    houses = House.objects.all()
    context = {'houses':houses}
    return render(request, 'LiYang/index.html', context)
