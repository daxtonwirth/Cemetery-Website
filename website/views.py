from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import Grave
from .forms import GraveForm

def home(request):
    all_people = Grave.objects.all
    return render(request, 'home.html', {'all':all_people})

def veterans(request):
    all_people = Grave.objects.all
    return render(request, 'veterans.html', {'all':all_people})

def add(request):
    if request.method == "POST":
        form = GraveForm(request.POST or None)
        if form.is_valid():
            form.save()
        return render(request, 'add.html', {})

    else:
        return render(request, 'add.html', {})
    
#def search(request):
#    all_people = Grave.objects.all
#    return render(request, 'search.html', {'all':all_people})

class SearchResultsView(ListView):
    model = Grave
    template_name = "search.html"

    def get_queryset(self):  
        query = self.request.GET.get("q")
        #query1 = self.request.GET.get("q1")
        object_list = Grave.objects.filter(
            FirstName__icontains=query 
            #last_name__icontains=query1
        )
        return object_list