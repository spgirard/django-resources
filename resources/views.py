### resources app views

from django.shortcuts import render
#   bring in models
from .models import Resource, Resource_Category
#   for db requests
from django.shortcuts import render, get_object_or_404

def list(request, category_slug=None):
    #   default 'all' list
    #   or by passed category slug
    resources = Resource.objects.all()
    categories = Resource_Category.objects.all()
    category = None

    if category_slug:
        category = get_object_or_404(Resource_Category, slug=category_slug)
        resources = Resource.objects.filter(category=category)

    context = {
        'category': category,
        'resources': resources,
        'categories': categories,
    }

    return render(request, 'resources/index.html', context)
