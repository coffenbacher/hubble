from django.shortcuts import render
from models import *

# Create your views here.

def index(request):
    conservatives = Suggestion.objects.filter(certainty__gte = 90)
    moderates = Suggestion.objects.filter(certainty__gte = 60)
    aggressives = Suggestion.objects.all()

    ss = Suggestion.objects.filter(ignore=False).order_by('-savings')
    return render(request, 'suggestions.html',
            {'ss': ss,
                'cc': Suggestion.calculate_savings(conservatives),   
                'mc': Suggestion.calculate_savings(moderates),   
                'ac': Suggestion.calculate_savings(aggressives),   
            })
