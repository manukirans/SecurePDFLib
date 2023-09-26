from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from pdf_box.models import category_choices, catalog_choices, File, Cart


# Create your views here.
def index(request):
    context = {
        "categories": category_choices,
        "catalogs": catalog_choices,
        "error": request.GET.get('error', "")
    }

    return render(request, "home/index.html", context=context)


def about(request):
    return render(request, "home/about.html")


def search(request):
    context = {
        "categories": category_choices,
        "catalogs": catalog_choices,
        "authors": File.objects.values_list('author', flat=True).distinct(),
        "books": File.objects.filter(
            file_name__icontains=request.GET.get('text', ''),
            category__icontains=request.GET.get('category', ''),
            catalog__icontains=request.GET.get('catalog', ''),
            author__icontains=request.GET.get('author', '')
        ),
        "text": request.GET.get('text', ''),
    }

    return render(request, "home/search.html", context=context)


@login_required(login_url='/auth/login')
def cart(request):
    user_cart, _ = Cart.objects.get_or_create(user=request.user)

    context = {
        "books": user_cart.books.all(),
    }
    return render(request, "home/cart.html", context=context)


@login_required(login_url='/auth/login')
def add_to_cart(request, file_id):
    user_cart, _ = Cart.objects.get_or_create(user=request.user)
    file = File.objects.get(pk=file_id)
    user_cart.books.add(file)

    return redirect("/kart")


@login_required(login_url='/auth/login')
def remove_book_from_cart(request, book_id):
    user_cart = Cart.objects.get(user=request.user)
    book = File.objects.get(pk=book_id)
    user_cart.books.remove(book)

    return redirect("/kart")

