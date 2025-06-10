from django.shortcuts import render

def first_view(request):
    return render(request, 'base.html')

def second_view(request):
    return render(request, 'about.html')

def contacts_view(request):
    return render(request, 'contacts.html')

def how_to_find_view(request):
    return render(request, 'how_to_find.html')

def categories_view(request):
    return render(request, 'categories.html')

def cats_view(request):
    return render(request, 'cats.html')

def dogs_view(request):
    return render(request, 'dogs.html')

def rodents_view(request):
    return render(request, 'rodents.html')

def all_products_view(request):
    return render(request, 'all_products.html')

def cart_view(request):
    return render(request, 'cart.html')