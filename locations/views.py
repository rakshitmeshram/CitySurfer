from django.shortcuts import render
from .models import Location


def location_list(request):
    locations = Location.objects.all()

    query = request.GET.get('search')
    if query:
        locations = locations.filter(name__icontains=query)

    context = {
        'locations': locations,
        'search_value': query,
    }

    return render(request, 'locations/location_list.html', context)


def location_detail(request, pk):
    location = Location.objects.get(pk=pk)

    context = {
        'location': location,
    }

    return render(request, 'locations/location_detail.html', context)
