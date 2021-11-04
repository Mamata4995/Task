from django.shortcuts import render,get_object_or_404,redirect
from django.utils import timezone
from product.models import Product
from product.forms import ProductForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView,ListView,DetailView,UpdateView,DeleteView,CreateView
# Create your views here.

class ProductView(TemplateView):
    template_name = 'product/product_basic.html'

class ProductListView(ListView):
    model = Product

    def get_queryset(self):
        return Product.objects.filter(updated_at__lte=timezone.now()).order_by('-updated_at')

class ProductDetailView(DetailView):
    model = Product

class ProductCreateView(LoginRequiredMixin,CreateView):
    login_url = '/login/'
    redirect_field_name = 'product/product_detail.html'
    form_class = ProductForm
    model = Product

class ProductUpdateView(LoginRequiredMixin,UpdateView):
    login_url = '/login/'
    redirect_field_name = 'product/product_detail.html'
    form_class = ProductForm
    model = Product

class ProductDeleteView(LoginRequiredMixin,DeleteView):
    model = Product
    success_url = reverse_lazy('product_list')

class DraftListView(LoginRequiredMixin,ListView):
    login_url = '/login/'
    redirect_field_name = 'product/product_draft_list.html'
    model = Product

    def get_queryset(self):
        return Product.objects.filter(updated_at__isnull=True).order_by('updated_at')


@login_required
def product_publish(request,pk):
    product = get_object_or_404(Product,pk=pk)
    product.publish()
    return redirect('product_detail',pk=pk)
