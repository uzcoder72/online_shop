from django.db.models import Q
from django.shortcuts import render, redirect

from shop.forms import CommentForm, OrderForm
from shop.models import Product, Comment, Category


# Create your views here.

def home_page(request,category_slug=None):

    search = request.GET.get('searching')
    if search:
        products = Product.objects.filter(Q(name__icontains=search))
    else:
        products = Product.objects.all()
        categories = Category.objects.all()
    if category_slug:
        products = products.filter(category__slug=category_slug)

    context = {'products': products,
               'categories': categories}
    return render(request, 'shop/home.html', context)


def detail_page(request, product_id: int):
    product = Product.objects.get(id=product_id)
    related_products = Product.objects.all()
    product_comments = Comment.objects.filter(product=product_id)

    form = CommentForm()
    form2 = OrderForm()

    comment1 = None
    order = None
    if request.method == 'POST':
        form = CommentForm(data=request.POST)

        name = request.POST['order_name']
        email = request.POST['order_email']
        quantity = request.POST['order_quantity']
        print(1)
        form2 = OrderForm(data={'name': name, 'email': email, 'quantity': quantity})
        print(2)
        if form.is_valid():
            comment1 = form.save(commit=False)
            comment1.product = product
            comment1.save()

        elif form2.is_valid():
            print(3)
            order = form2.save(commit=False)
            order.product = product
            order.save()
            print(4)

    else:
        form = CommentForm()

    context = {'product': product,
               'related_products': related_products,
               'product_comments': product_comments,
               'form': form,
               'form2': form2}
    return render(request, 'shop/detail.html', context)


def about_page(request):
    return render(request, 'about/about.html')

def product_detail(request, slug):
    product = Product.objects.get(slug=slug)
    comments = Comment.objects.filter(product__slug=slug)
    new_comment = None  # Comment posted
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.product = product
            new_comment.save()
    else:
        comment_form = CommentForm()
    return render(request, 'shop/detail.html', {'product': product,
                                                'comments': comments,
                                                'new_comment': new_comment,
                                                'comment_form': comment_form})
