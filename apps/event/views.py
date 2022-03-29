from django.shortcuts import get_object_or_404, render

from .models import Event


def event_detail(request, pk):
    context = {"event": get_object_or_404(Event, pk=pk)}
    return render(request, "event_detail.html", context)
