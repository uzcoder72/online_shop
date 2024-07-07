from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from shop.forms import CommentForm, OrderForm
from shop.models import Product, Comment, Category
from django.contrib import messages

# Create your views here.


from django.core.paginator import Paginator

def home_page(request, category_slug=None):
    search = request.GET.get('searching')
    categories = Category.objects.all()
    products = Product.objects.all()

    if search:
        products = products.filter(name__icontains=search)

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)

    # Sorting logic
    expensive = request.GET.get('expensive')
    cheap = request.GET.get('cheap')

    if expensive:
        products = products.order_by('-price')
    elif cheap:
        products = products.order_by('price')

    # Pagination logic
    paginator = Paginator(products, 12)  # Show 12 products per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'categories': categories,
    }
    return render(request, 'shop/home.html', context)





def detail_page(request, product_id: int,en_slug):
    product = Product.objects.get(id=product_id)
    related_products = Product.objects.filter(Q(category=product.category) & Q(is_available=True)).exclude(
        Q(slug=en_slug) | Q(quantity=0))
    product_comments = Comment.objects.filter(product=product_id).order_by('-created_at')

    form = CommentForm()
    form2 = OrderForm()

    if request.method == 'POST':
        if 'order_name' in request.POST and 'order_email' in request.POST and 'order_quantity' in request.POST:
            form2 = OrderForm(data={
                'name': request.POST['order_name'],
                'related_products': related_products,
                'email': request.POST['order_email'],
                'quantity': request.POST['order_quantity']
            })
            if form2.is_valid():
                order = form2.save(commit=False)
                order.product = product
                order.save()
                messages.success(request, 'Your order was successfully submitted.')
        else:
            form = CommentForm(data=request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.product = product
                comment.save()
                messages.success(request, 'Your comment was successfully submitted.')
                return redirect('detail', product_id=product_id)

    context = {
        'product': product,
        'related_products': related_products,
        'product_comments': product_comments,
        'form': form,
        'form2': form2,
    }
    return render(request, 'shop/detail.html', context)







def about_page(request):
    return render(request, 'about/about.html')



def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    comments = Comment.objects.filter(product=product).order_by('-created_at')
    related_products = Product.objects.filter(Q(category=product.category) & Q(is_available=True)).exclude(
        Q(slug=slug) | Q(quantity=0))


    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.product = product
            comment.save()
            return redirect('product_detail', slug=product.slug)
    else:
        form = CommentForm()

    context = {
        'product': product,
        'related_products': related_products,
        'product_comments': comments,
        'form': form,
    }
    return render(request, 'shop/detail.html', context)


# views.py

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from shop.models import Product


@login_required
def delete_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    if request.method == 'POST':
        product.delete()
        return redirect('index')

    context = {
        'product': product,
    }
    return render(request, 'delete_product.html', context)



