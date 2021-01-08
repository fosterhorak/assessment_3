from django.shortcuts import render
from .models import Widget
from .forms import WidgetForm

# Create your views here.
def index(request):
    widgets = Widget.objects.all()
    add_widget_form = WidgetForm()

    return render(request, 'index.html', {
        'widgets': widgets, 
        'add_widget_form': add_widget_form
    })
