from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Category, Cart, Cart_Item
from accounts.models import User_Profile
from django.http import HttpResponse, JsonResponse
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from website.forms import UserFeedbackForm


@login_required(login_url='Login')
def home(request):
    CategoryItems = Category.objects.all()
    Apparel = Product.objects.all().order_by('?')
    context = {'CategoryItems': CategoryItems, 'Apparels': Apparel}
    return render(request, 'Home.html', context)


@login_required(login_url='Login')
def Category_Product_listing(request, foo):
    foo = foo.replace('-', '')
    category = Category.objects.get(CID=foo)
    products = Product.objects.filter(category=category)
    context = {'Category': category, 'Products': products}
    return render(request, 'Category.html', context)


@login_required(login_url='Login')
def Search_Apparel(request):
    if request.method == 'POST':
        Search = request.POST['Searched']

        Items = Product.objects.filter(name__icontains=Search,)
        context = {'Searched': Search, 'Item': Items}
        return render(request, 'Search_Apparel.html', context)
    else:
        return render(request, 'Search_Apparel.html')


@login_required(login_url='Login')
def Products_Page(request):
    Apparel = Product.objects.all().order_by('?')
    context = {'Apparels': Apparel}
    return render(request, 'Products.html', context)


@login_required(login_url='Login')
def CartPage(request, total=0, quantity=0, cart_items=None):
    try:
        cart = Cart.objects.get(Cart_Id=_CartID(request))
        cart_items = Cart_Item.objects.filter(
            cart=cart)  # Got the Cart Items
        for cart_item in cart_items:  # Looping through the cart items
            total += (cart_item.product.price * cart_item.quantity)
            quantity += cart_item.quantity

    except ObjectDoesNotExist:
        pass

    context = {'cart_items': cart_items, 'total': total, 'quantity': quantity}
    return render(request, 'cart.html', context)


@login_required(login_url='Login')
def _CartID(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
        print('ID: ', cart)
    return cart


@login_required(login_url='Login')
def add_to_cart(request, pk):
    product = Product.objects.get(id=pk)

    try:
        cart = Cart.objects.get(Cart_Id=_CartID(request))

    except Cart.DoesNotExist:
        cart = Cart.objects.create(
            Cart_Id=_CartID(request)
        )
        cart.save()

    try:
        cart_Item = Cart_Item.objects.get(product=product, cart=cart)
        cart_Item.quantity += 1
        cart_Item.save()

    except Cart_Item.DoesNotExist:
        cart_Item = Cart_Item.objects.create(
            product=product,
            quantity=1,
            cart=cart,
        )
        cart_Item.save()
    return redirect('cart')

    # return render(request, 'cart.html')


@login_required(login_url='Login')
def remove_from_cart(request, pk):
    product = get_object_or_404(Product, id=pk)
    cart = Cart.objects.get(Cart_Id=_CartID(request))
    cart_Item = Cart_Item.objects.get(product=product, cart=cart)
    if cart_Item.quantity > 1:
        cart_Item.quantity -= 1
        cart_Item.save()

    else:
        cart_Item.delete()
        return redirect('cart')
    return redirect('cart')


@login_required(login_url='Login')
def Delete_from_cart(request, pk):
    product = get_object_or_404(Product, id=pk)
    cart = Cart.objects.get(Cart_Id=_CartID(request))
    cart_Item = Cart_Item.objects.get(product=product, cart=cart)
    cart_Item.delete()
    return redirect('cart')


def About(request):
    User_feedback = UserFeedbackForm()
    if request.method == "POST":
        User_feedback = UserFeedbackForm(request.POST)
        if User_feedback.is_valid():
            User_feedback.save()
        return redirect('about')
    context = {'FeedbackForm': User_feedback}
    return render(request, 'About.html', context)


@login_required(login_url='Login')
def ProductDetails(request, pk):
    Apparels = Product.objects.get(id=pk)
    context = {'Apparel': Apparels}
    return render(request, 'ProductDetails.html', context)
