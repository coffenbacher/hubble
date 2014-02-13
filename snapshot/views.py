from django.shortcuts import render, redirect
from snapshot.models import *
from suggestion.models import *

# Create your views here.

def index(request):
    real_suggestions = Suggestion.objects.all()
    pks = list(real_suggestions.values_list('cosmosdir', flat=True))
    for r in real_suggestions:
        pks.extend(r.cosmosdir.all_children_pks())

    print pks
    dirs = CosmosDir.objects.exclude(pk__in=pks).order_by('-score_deletion')[:100]
    return render(request, 'index.html', {'dirs': dirs.select_related()})

def suggest(request, cd):
    cosmosdir = CosmosDir.objects.get(pk=cd)
    if request.method == 'POST':
        form = SuggestionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/snapshot/') 
    else:
        s = Suggestion(cosmosdir = cosmosdir)
        form = SuggestionForm(instance = s)
    return render(request, 'create.html', {'form': form, 'd': cosmosdir})

def approve(request, cd):
    cosmosdir = CosmosDir.objects.get(pk=cd)
    s = Suggestion(cosmosdir = cosmosdir, ignore = True)
    s.save()
    return redirect('/snapshot/')