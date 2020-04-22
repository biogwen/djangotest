from django.shortcuts import render
from .models import formulairetest as fmr
from django.utils import timezone

# Create your views here.


def rendu:
    rendus = fmr.objects.filter(champ_date=timezone.now()).order_by('champ_decimal')
    return render(request, 'rendu.html', {})