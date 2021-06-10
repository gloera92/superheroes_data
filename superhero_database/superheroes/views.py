from django.shortcuts import render
from .models import Superhero
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
# Create your views here.


def index(request):
    all_superheroes = Superhero.objects.all()
    context = {
        'all_superheroes': all_superheroes
    }
    return render(request, 'superheroes/index.html', context)


def detail(request, superhero_id):
    pick_superhero = Superhero.objects.get(pk=superhero_id)
    context = {
        'Superhero': pick_superhero
    }
    return render(request, 'superheroes/detail.html', context)


def create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        alter_ego = request.POST.get('alter_ego')
        primary_ability = request.POST.get('primary_ability')
        alternate_ability = request.POST.get('alternate_ability')
        catchphrase = request.POST.get('catchphrase')
        new_superhero = Superhero(name=name, alter_ego=alter_ego, primary_ability=primary_ability,
                                  alternate_ability=alternate_ability, catchphrase=catchphrase,)
        new_superhero.save()
        return HttpResponseRedirect(reverse('superheroes:index'))
    else:
        return render(request, 'superheroes/create.html')


