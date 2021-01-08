from django.shortcuts import render, redirect
from django.db.models import Count, Avg
from .models import Widget
from .forms import WidgetForm

# Create your views here.
def index(request):
    widgets = Widget.objects.all()
    add_widget_form = WidgetForm()
    quantity_avg = Widget.objects.all().aggregate(Avg('quantity'))
    quantity_count = Widget.objects.all().aggregate(Count('quantity'))
    quantity_total = 10

    return render(request, 'index.html', {
        'widgets': widgets, 
        'add_widget_form': add_widget_form,
        # 'quantity_total': quantity_total,
        # 'quantity_avg': quantity_avg.quantity_avg,
        # 'quantity_count': quantity_count.quantity_count,
    })

def add_widget(request):
    form = WidgetForm(request.POST)

    if form.is_valid():
        new_widget = form.save()
    
    # widgets = Widget.objects.all()
    # return redirect('index', widgets = widgets)

    return redirect('/')



def delete_widget(request, widget_id):
    Widget.objects.get(id=widget_id).delete()
    return redirect('/')