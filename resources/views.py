### resources app views

from django.shortcuts import render
#   bring in models
from .models import Resource, Resource_Category
#   for db requests
from django.shortcuts import render, get_object_or_404

def list(request, category_slug=None, resources={}):
    #   default 'all' list
    #   or by passed category slug
    resources = Resource.objects.all()
    categories = Resource_Category.objects.all()
    category = None
    resource_list = {}

    #   resources by category
    for cat in categories:
        #   create a list in the dictionary for each category with the resources
        category_resources = Resource.objects.filter(category=cat)
        resource_list[cat.category] = category_resources

    if category_slug:
        category = get_object_or_404(Resource_Category, slug=category_slug)
        resources = Resource.objects.filter(category=category)

    #   gather context
    context = {
        'category': category,
        'resources': resources,        
        'categories': categories,                
        'resource_list': resource_list,
    }

    return render(request, 'resources/index.html', context)

