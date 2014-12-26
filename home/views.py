from django.shortcuts import render
from shops.models import Item
from shops.models import Category
#import django.core.paginator.Paginator
from django.template import RequestContext
from django.shortcuts import render_to_response
from endless_pagination.decorators import page_template
from django.views.decorators.csrf import csrf_exempt
import json
import pdb;
@csrf_exempt
@page_template("index_page.html") # just add this decorator
def index(request, template="index.html",
    extra_context=None):

    if request.POST and request.POST['search'] == "true":
        # pdb.set_trace();
        items = Item.objects.filter(category_id__in =json.loads(request.POST['item_id']))
        context= {
            'all_items': items,
	        'categories' : Category.objects.all(),
        }
    else:
        context = {
	        'all_items': Item.objects.all(),
	        'categories' : Category.objects.all(),
	    }
        #pdb.set_trace()
    if extra_context is not None:
        context.update(extra_context)
    return render_to_response(template, context,
        context_instance=RequestContext(request))
    #return render(request, 'index.html', context)