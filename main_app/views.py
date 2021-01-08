from django.shortcuts import render, redirect
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

def add_widget(request):
    form = WidgetForm(request.POST)
    print('add_widget function is running')

    if form.is_valid():
        new_widget = form.save()
    
    # widgets = Widget.objects.all()
    # return redirect('index', widgets = widgets)

    return redirect('/')



def delete_widget(request, widget_id):
    Widget.objects.get(id=widget_id).delete()
    return redirect('/')