from django.contrib.auth.decorators import permission_required
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from .models import *
from .forms import *
from basket.forms import BasketAddProductForm
from django.contrib.auth import login, logout


def first_view(request):
    return render(request, 'index.html')

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

def all_products(request):
    catalog_product = CatalogProduct.objects.all()
    form_basket = BasketAddProductForm()
    return render(request, 'all_products.html', {
        'catalog_product': catalog_product,
        'form_basket': form_basket,
    })

def cart_view(request):
    return render(request, 'cart.html')

# class ClothesListView(ListView):
#     model = Clothes
#     template_name = 'clothes/clothes_list.html'
#     context_object_name = 'clothes'
#
# class ClothesDetailView(DetailView):
#     model = Clothes
#     template_name = 'clothes/clothes_detail.html'
#     context_object_name = 'clothes'
#
#
# class ClothesCreateView(CreateView):
#     model = Clothes
#     form_class = ClothesForm
#     template_name = 'clothes/clothes_form.html'
#     success_url = reverse_lazy('clothes_list_view')
#
# class ClothesUpdateView(UpdateView):
#     model = Clothes
#     form_class = ClothesForm
#     template_name = 'clothes/clothes_form.html'
#     success_url = reverse_lazy('clothes_list_view')
#
# class ClothesDeleteView(DeleteView):
#     model = Clothes
#     context_object_name = 'clothes'
#     template_name = 'clothes/clothes_confirm_delete.html'
#     success_url = reverse_lazy('clothes_list_view')

class BrandListView(PermissionRequiredMixin, ListView):
    permission_required = 'shop.read_brand'
    model = Brand
    template_name = 'brand/brand_list.html'
    context_object_name = 'brand'

class BrandDetailView(PermissionRequiredMixin, DetailView):
    permission_required = 'shop.read_brand'
    model = Brand
    template_name = 'brand/brand_detail.html'
    context_object_name = 'brand'

class BrandCreateView(PermissionRequiredMixin, CreateView):
    permission_required = 'shop.create_brand'
    model = Brand
    form_class = BrandsForm
    template_name = 'brand/brand_form.html'
    success_url = reverse_lazy('brand_list_view')

class BrandUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = 'shop.update_brand'
    model = Brand
    form_class = BrandsForm
    template_name = 'brand/brand_form.html'
    success_url = reverse_lazy('brand_list_view')

class BrandDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = 'shop.delete_brand'
    model = Brand
    context_object_name = 'brand'
    template_name = 'brand/brand_confirm_delete.html'
    success_url = reverse_lazy('brand_list_view')

class CategoryProductListView(PermissionRequiredMixin, ListView):
    permission_required = 'shop.read_categoryproduct'
    model = CategoryProduct
    template_name = 'categoryproduct/category_list.html'
    context_object_name = 'category_product'

class CategoryProductDetailView(PermissionRequiredMixin, DetailView):
    permission_required = 'shop.read_categoryproduct'
    model = CategoryProduct
    template_name = 'categoryproduct/catgory_detail.html'
    context_object_name = 'category_product'

class CategoryProductCreateView(PermissionRequiredMixin, CreateView):
    permission_required = 'shop.create_categoryproduct'
    model = CategoryProduct
    form_class = CategoryProductForm
    template_name = 'categoryproduct/category_forms.html'
    success_url = reverse_lazy('category_product_list_view')

class CategoryProductUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = 'shop.update_categoryproduct'
    model = CategoryProduct
    form_class = CategoryProductForm
    template_name = 'categoryproduct/category_forms.html'
    success_url = reverse_lazy('category_product_list_view')

class CategoryProductDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = 'shop.delete_categoryproduct'
    model = CategoryProduct
    context_object_name = 'categoryproduct'
    template_name = 'category_product/category_delete_confirm.html'
    success_url = reverse_lazy('category_product_list_view')

class PetTypeListView(PermissionRequiredMixin, ListView):
    permission_required = 'shop.read_pettype'
    model = PetType
    template_name = 'pettype/pet_type_list.html'
    context_object_name = 'pet_type'

class PetTypeDetailView(PermissionRequiredMixin, DetailView):
    permission_required = 'shop.read_pettype'
    model = PetType
    template_name = 'pettype/pet_type_detail.html'
    context_object_name = 'pet_type'

class PetTypeCreateView(PermissionRequiredMixin, CreateView):
    permission_required = 'shop.create_pettype'
    model = PetType
    form_class = PetTypeForm
    template_name = 'pettype/pet_type_form.html'
    success_url = reverse_lazy('pet_type_list_view')

class PetTypeUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = 'shop.update_pettype'
    model = PetType
    form_class = PetTypeForm
    template_name = 'pettype/pet_type_form.html'
    success_url = reverse_lazy('pet_type_list_view')

class PetTypeDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = 'shop.delete_pettype'
    model = PetType
    context_object_name = 'pet_type'
    template_name = 'pettype/pet_type_confirm_delete.html'
    success_url = reverse_lazy('pet_type_list_view')

class PromotionListView(PermissionRequiredMixin, ListView):
    permission_required = 'shop.read_promotion'
    model = Promotion
    template_name = 'promotion/promotion_list.html'
    context_object_name = 'promotion'

class PromotionDetailView(PermissionRequiredMixin, DetailView):
    permission_required = 'shop.read_promotion'
    model = Promotion
    template_name = 'promotion/promotion_detail.html'
    context_object_name = 'promotion'

class PromotionCreateView(PermissionRequiredMixin, CreateView):
    permission_required = 'shop.create_promotion'
    model = Promotion
    form_class = PromotionForm
    template_name = 'promotion/promotion_form.html'
    success_url = reverse_lazy('promotion_list_view')

class PromotionUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = 'shop.update_promotion'
    model = Promotion
    form_class = PromotionForm
    template_name = 'promotion/promotion_form.html'
    success_url = reverse_lazy('promotion_list_view')

class PromotionDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = 'shop.delete_promotion'
    model = Promotion
    context_object_name = 'promotion'
    template_name = 'promotion/promotion_confirm_delete.html'
    success_url = reverse_lazy('promotion_list_view')

class CatalogProductListView(PermissionRequiredMixin, ListView):
    permission_required = 'shop.read_catalogproduct'
    model = CatalogProduct
    template_name = 'catalogproduct/catalog_product_list.html'
    context_object_name = 'catalog_product'

class CatalogProductDetailView(PermissionRequiredMixin, DetailView):
    permission_required = 'shop.read_catalogproduct'
    model = CatalogProduct
    template_name = 'catalogproduct/catalog_product_detail.html'
    context_object_name = 'catalog_product'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_basket'] = BasketAddProductForm()
        return context

class CatalogProductCreateView(PermissionRequiredMixin, CreateView):
    permission_required = 'shop.create_catalogproduct'
    model = CatalogProduct
    form_class = CatalogProductForm
    template_name = 'catalogproduct/catalog_product_form.html'
    success_url = reverse_lazy('catalog_product_list_view')

class CatalogProductUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = 'shop.update_catalogproduct'
    model = CatalogProduct
    form_class = CatalogProductForm
    template_name = 'catalogproduct/catalog_product_form.html'
    success_url = reverse_lazy('catalog_product_list_view')

class CatalogProductDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = 'shop.delete_catalogproduct'
    model = CatalogProduct
    context_object_name = 'catalog_product'
    template_name = 'catalogproduct/catalog_product_confirm_delete.html'
    success_url = reverse_lazy('catalog_product_list_view')


def login_user(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            if request.GET.get('next'):
                return redirect(request.GET.get('next'))
            return redirect('catalog_product_list_view')
    else:
        form = LoginForm()
    return render(request, 'auth/login.html', context={'form': form})


def registration_user(request):
    if request.method == 'POST':
        form = RegistrationForm(data=request.POST)
        if form.is_valid():
            login(request, form.save())
            if request.GET.get('next'):
                return redirect(request.GET.get('next'))
            return redirect('catalog_product_list_view')
    else:
        form = RegistrationForm()
    return render(request, 'auth/registration.html', context={'form': form})

def logout_user(request):
    logout(request)
    return redirect('catalog_product_list_view')