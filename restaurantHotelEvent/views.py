from django.shortcuts import render, redirect, get_object_or_404

from .models import Restaurant, Hotel, Event
from .forms import RestaurantForm, HotelForm, EventForm
from django.contrib import messages

def admin_dashboard(request):
    if not request.user.is_staff:  # Vérifie si l'utilisateur est un administrateur
        return redirect('login')

    restaurants = Restaurant.objects.all()
    hotels = Hotel.objects.all()
    events = Event.objects.all()

    context = {
        'restaurants': restaurants,
        'hotels': hotels,
        'events': events
    }
    return render(request, 'admin_dashboard.html', context)

def add_restaurant(request):
    if not request.user.is_staff:
        messages.error(request, 'Vous devez être administrateur pour accéder à cette page.')
        return redirect('login')
    
    if request.method == 'POST':
        form = RestaurantForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Restaurant créé avec succès.')
            return redirect('admin_dashboard')
    else:
        form = RestaurantForm()

    return render(request, 'add_restaurant.html', {'form': form})

def add_hotel(request):
    if not request.user.is_staff:
        return redirect('login')
    
    if request.method == 'POST':
        form = HotelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Hôtel créé avec succès.')
            return redirect('admin_dashboard')
    else:
        form = HotelForm()

    return render(request, 'add_hotel.html', {'form': form})

def add_event(request):
    if not request.user.is_staff:
        return redirect('login')
    
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Evenement créé avec succès.')
            return redirect('admin_dashboard')
    else:
        form = EventForm()

    return render(request, 'add_event.html', {'form': form})

# Vue pour afficher les détails d'un restaurant
def restaurant_detail(request, restaurant_id):
    restaurant = get_object_or_404(Restaurant, id=restaurant_id)
    return render(request, 'restaurant_detail.html', {'restaurant': restaurant})

# Vue pour afficher les détails d'un hôtel
def hotel_detail(request, hotel_id):
    hotel = get_object_or_404(Hotel, id=hotel_id)
    return render(request, 'hotel_detail.html', {'hotel': hotel})

# Vue pour afficher les détails d'un événement
def event_detail(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    return render(request, 'event_detail.html', {'event': event})

def update_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    if request.method == "POST":
        form = EventForm(request.POST, request.FILES, instance=event)
        if form.is_valid():
            form.save()
            return redirect('event_detail', event_id=event.id)
    else:
        form = EventForm(instance=event)
    return render(request, 'update_event.html', {'form': form, 'event': event})

def delete_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    if request.method == "POST":
        event.delete()
        messages.success(request, 'Événement supprimé avec succès.')
        return redirect('admin_dashboard')
    return render(request, 'confirm_delete.html', {'event': event})



def update_hotel(request, id):
    hotel = get_object_or_404(Hotel, id=id)
    if request.method == 'POST':
        form = HotelForm(request.POST, request.FILES, instance=hotel)
        if form.is_valid():
            form.save()
            messages.success(request, 'Hôtel mis à jour avec succès.')
            return redirect('admin_dashboard') # Use 'hotel_id' here
    else:
        form = HotelForm(instance=hotel)
    return render(request, 'hotel_update.html', {'form': form, 'hotel': hotel})


def delete_hotel(request, hotel_id):
    hotel = get_object_or_404(Hotel, id=hotel_id)
    if request.method == "POST":
        hotel.delete()
        messages.success(request, 'Hôtel supprimé avec succès.')
        return redirect('admin_dashboard')
    return render(request, 'confirm_delete.html', {'hotel': hotel})


def update_restaurant(request, id):
    restaurant = get_object_or_404(Restaurant, id=id)
    if request.method == 'POST':
        form = RestaurantForm(request.POST, request.FILES, instance=restaurant)
        if form.is_valid():
            form.save()
            messages.success(request, 'Restaurant mis à jour avec succès.')
            return redirect('admin_dashboard')
    else:
        form = RestaurantForm(instance=restaurant)
    return render(request, 'restaurant_update.html', {'form': form, 'restaurant': restaurant})

def delete_restaurant(request, restaurant_id):
    restaurant = get_object_or_404(Restaurant, id=restaurant_id)
    if request.method == "POST":
        restaurant.delete()
        messages.success(request, 'Restaurant supprimé avec succès.')
        return redirect('admin_dashboard')
    return render(request, 'confirm_delete.html', {'restaurant': restaurant})

