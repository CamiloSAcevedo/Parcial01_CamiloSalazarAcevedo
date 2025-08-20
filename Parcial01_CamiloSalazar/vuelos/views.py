from django.shortcuts import render, redirect
from django.db.models import Avg
from .models import Flight
from .forms import FlightForm

def home(request):
    return render(request, 'vuelos/home.html')

def crear_vuelo(request):
    if request.method == 'POST':
        form = FlightForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list')
    else:
        form = FlightForm()
    return render(request, 'vuelos/create.html', {'form': form})

def listar_vuelos(request):
    flights = Flight.objects.order_by('price') 
    return render(request, 'vuelos/list.html', {'flights': flights})

def estadisticas(request):
    nationales = Flight.objects.filter(type=Flight.NACIONAL)
    internationales = Flight.objects.filter(type=Flight.INTERNACIONAL)

    data = {
        'count_national': nationales.count(),
        'count_international': internationales.count(),
        'avg_national_price': nationales.aggregate(Avg('price'))['price__avg'],
    }
    return render(request, 'vuelos/stats.html', data)
