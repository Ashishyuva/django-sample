from django.shortcuts import render
from shops.models import Item
#import django.core.paginator.Paginator
from django.template import RequestContext
from django.shortcuts import render_to_response
from endless_pagination.decorators import page_template
import pdb;
@page_template("index_page.html") # just add this decorator
def index(request, template="index.html",
    extra_context=None):
    context = {
        'all_items': Item.objects.all(),
    }
    if extra_context is not None:
        context.update(extra_context)
    return render_to_response(template, context,
        context_instance=RequestContext(request))