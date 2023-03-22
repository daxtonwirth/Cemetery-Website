from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView
from .models import Grave
from .forms import GraveForm
from django.contrib import messages
from django.db.models import Q 


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
    

class SearchResultsView(ListView):
    model = Grave
    template_name = "search.html"

    def get_queryset(self):  
        query = self.request.GET.get("q")
        if " " in query:
            term = query.split()
            object_list = Grave.objects.filter(Q(Occupant__icontains=term[0]) & Q(Occupant__icontains=term[1]))
        else:
            term = query
            object_list = Grave.objects.filter(Q(Occupant__icontains=term) | Q(Occupant__icontains=term))
        return object_list
    
    
    
    
    
import googlemaps
from django.shortcuts import render

def map_view(request):
    # Create a client with the API key
    gmaps = googlemaps.Client(key='AIzaSyBQZ0MOCrRpEhYwjgsXisPvJ98Ajn0fFAw')

    # Make a request to the Google Maps API to retrieve data
    data = gmaps.geocode('4023 Ririe Hwy, Rigby, ID 83442')

    # Extract the latitude and longitude from the data
    lat = data[0]['geometry']['location']['lat']
    lng = data[0]['geometry']['location']['lng']

    # Render the template with the latitude and longitude
    return render(request, 'home.html', {'lat': lat, 'lng': lng})