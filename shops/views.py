from django.shortcuts import get_object_or_404, render
from django.shortcuts import render_to_response
from shops.models import Shop
from shops.models import Product
from shops.models import Item
from django.core.files import File
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger#import settings
import stripe
from django.views.decorators.csrf import ensure_csrf_cookie
import pdb;
def new(request):

    return render(request, 'shops/create.html')
    #create method
def create(request):
    # If this is a post request we insert the person
    if request.POST:
        shop = Shop(name=request.POST['name'],description=request.POST['description'],address=request.POST['address'],zip_code=request.POST['zip_code'],city=request.POST['city'],state=request.POST['state'],country=request.POST['country'])
        shop.save()
        all_shops = Shop.objects.all()
        context = {'all_shops': all_shops}
     
    return render(request, 'shops/all_shops.html', context) 

def all_shops(request):
    all_shops = Shop.objects.all()
    context = {'all_shops': all_shops}
    return render(request, 'shops/all_shops.html', context) 

def new_product(request):
    shops = Shop.objects.filter()
    context = {'shops' : shops}
    return render(request, 'shops/new_product.html', context)

def create_product(request):
    if request.POST:
        product = Product(name=request.POST['name'],description=request.POST['description'])
        product.save()
        shop  = Shop.objects.get(id=request.POST['shop_id'])
        product.shop_set.add(shop)
        all_products = Product.objects.all()
        context = {'all_products': all_products}
    return render(request, 'shops/all_products.html', context) 

def all_products(request):
    all_products = Product.objects.all()
    context = {'all_products': all_products}
    return render(request, 'shops/all_products.html', context) 

def new_item(request):
    shops = Shop.objects.filter()
    products = Product.objects.filter()
    context = {'shops' : shops,'products' : products}
    return render(request, 'shops/new_item.html', context)

def create_item(request):
    if request.POST:
        item = Item(name=request.POST['name'],description=request.POST['description'],image=request.FILES['image'])
        shop  = Shop.objects.get(id=request.POST['shop_id'])
        product = Product.objects.get(id=request.POST['product_id'])
        item.shop = shop
        item.product = product
        item.save()
        all_items = Item.objects.all()
        context = {'all_items': all_items}
    return render(request, 'shops/all_items.html', context)

def all_items(request):
    items = Item.objects.filter()
    paginator = Paginator(items, 9)
    page = request.GET.get('page')
    try:
        items = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        items = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        items = paginator.page(paginator.num_pages)
    return render(request, 'shops/all_items.html', {'items': items})

def item_detail(request, item_id):
    try:
        item = Item.objects.get(pk=item_id)
    except Item.DoesNotExist:
        raise Http404
    return render(request, 'shops/item_detail.html',  {'item': item})

def payment_model(request, item_id):
    try:
        item = Item.objects.get(pk=item_id)
    except Item.DoesNotExist:
        raise Http404
    return render(request,'shops/payment_model.html',  {'item': item})

def create_payment_stripe(request, item_id):
    item = Item.objects.get(pk=item_id)
    stripe.api_key = "sk_test_tBcbnfnWfCmoTjN0DWCIAhi9"
    # Get the credit card details submitted by the form
    token =  request.POST['stripe_token']
    try:
        charge = stripe.Charge.create(
            amount=1000, # amount in cents, again
            currency="usd",
            card=token,
            description="payinguser@example.com"
         )
    except stripe.CardError, e:
     # The card has been declined
        pass
    return render(request, 'shops/item_detail.html',  {'item': item})

def delete_item(request,item_id):
    item = Item.objects.get(pk=item_id)
    item.delete()
    items = Item.objects.all()
    return render(request, 'shops/all_items.html',  {'items': items})

def edit_item(request,item_id):
    shops = Shop.objects.filter()
    products = Product.objects.filter()
    item = Item.objects.get(pk=item_id)
    context = {'shops' : shops,'products' : products,'item' : item}
    return render(request, 'shops/edit.html', context)

def update_item(request):
    item = Item.objects.get(pk=request.POST['item_id'])
    item.name = request.POST['name']
    item.description = request.POST['description']
  #  item.image = request.FILES['image']
    item.save()
    shop  = Shop.objects.get(id=request.POST['shop_id'])
    product = Product.objects.get(id=request.POST['product_id'])
    item.shop = shop
    item.product = product
    item.save()
    items = Item.objects.filter()
    paginator = Paginator(items, 9)
    page = request.GET.get('page')
    try:
        items = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        items = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        items = paginator.page(paginator.num_pages)
    return render(request, 'shops/all_items.html',  {'items': items})
