from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView
from .models import Grave
from .forms import GraveForm
from django.contrib import messages
from django.db.models import Q 


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
            messages.success(request, ("Added Successfully"))
            return redirect('home')
        else:
            #FirstName = request.POST["FirstName"]
            messages.success(request, ("Error, please try again"))
            render(request, 'add.html', {})

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
        term = query.split()
        object_list = Grave.objects.filter(Q(FirstName__icontains=term[0]) & Q(LastName__icontains=term[1]))
        return object_list