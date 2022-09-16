from operator import attrgetter

from django.db.models import F
from django.shortcuts import render
from ImmoApp.models.program import Program
from ImmoApp.models.models import Appartement
from django.utils.timezone import now


def list_appartements(request):
    programs = Program.objects.filter(dispo=True).values_list('prog_id', flat=True)
    apparts = Appartement.objects.filter(prog__in=list(programs)).values()
    context = {'apparts': apparts, 'title': 'liste des appartements (program actif)'}
    return render(request, 'template.html', context)


def list_appartements_prix(request):
    apparts = Appartement.objects.filter(prix__gte=100, prix__lte=180).values()
    print("rrrrrrrrrrrrr", type(apparts))
    context = {'apparts': apparts, 'title': 'liste des appartements prix'}
    return render(request, 'template.html', context)


def list_appartements_piscine(request):
    apparts = Appartement.objects.filter(caract__contains='piscine').values()
    context = {'apparts': apparts, 'title': 'liste des appartements piscine'}
    return render(request, 'template.html', context)


def list_appartements_promo(request):
    apparts = Appartement.objects.annotate(new_prix=F('prix') - F('prix') * 0.2).values()
    context = {'apparts': apparts, 'title': 'liste des appartements prix'}
    return render(request, 'template.html', context)


def sort_apparts(apparts,to_search):
    l_true = []
    l_false = []
    for i in list(apparts):
        l_true.append(i) if to_search in i['caract'] else l_false.append(i)
        apparts = l_true + l_false
        apparts = sorted(apparts, key=lambda k: (-k['prix'], -k['surface']))
        return apparts


def list_appartements_saison(request):
    apparts = Appartement.objects.all().values()
    if now().month in [12, 1, 2, 3]:
        sort_apparts(apparts, 'proche station ski')
    elif now().month in [6, 7, 8, 9]:
        sort_apparts(apparts, 'piscine')
    else:
        apparts = sorted(list(apparts), key=lambda k: (-k['prix'], -k['surface']))
    context = {'apparts': apparts, 'title': 'liste des appartements par saison'}
    return render(request, 'template.html', context)
