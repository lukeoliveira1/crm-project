from django.shortcuts import redirect, render, get_object_or_404

from crm.models import Product, Sale, Company

from crm.forms import ProductForm, SaleForm

from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'crm/index.html')

def products(request):
    products = Product.objects.order_by("name").all()
    return render(request, 'crm/products/products.html', {"products": products})

def product_by_id(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'crm/products/product_id.html', {"product": product})

def create_product(request):
    form = ProductForm
    
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            messages.success(request, 'Produto cadastrado com sucesso')
            return redirect('index')
        
    return render(request, 'crm/products/new_product.html', {'form': form})

def edit_product(request, product_id):
    product = Product.objects.get(id=product_id)

    form = ProductForm(instance=product)

    if request.method == 'POST':

        form = ProductForm(request.POST, request.FILES, instance=product)

        if form.is_valid():
            form.save()
            messages.success(request, 'Produto editado com sucesso')
            return redirect('index')
        
    return render(request, 'crm/products/edit_product.html', {'form': form, 'product_id': product_id})

def delete_product(request, product_id):
    product = Product.objects.get(id=product_id)
    product.delete()
    messages.success(request, 'Produto excluído com sucesso')
    return redirect('index')
    
def sales(request):
    sales = Sale.objects.order_by("sale_date").all()
    return render(request, 'crm/sales/sales.html', {"sales": sales})

def sale_by_id(request, sale_id):
    sale = get_object_or_404(Sale, pk=sale_id)
    return render(request, 'crm/sales/sale_id.html', {"sale": sale})

def create_sale(request):
    form = SaleForm

    if request.method == 'POST':
        form = SaleForm(request.POST)

        product_id = form['product'].value()
        quantity_sold = form['quantity_sold'].value()

        company = Company.objects.get(id=1)
        product = Product.objects.get(id=product_id)
        
        if form.is_valid():
            

            if int(product.quantity) >= int(quantity_sold):
                # add on financial of company
                company.total_revenue += (int(product.price) * int(quantity_sold))
                # remove quantity_sold from product
                product.quantity -= int(quantity_sold)

                form.save()
                product.save()
                company.save()
                messages.success(request, 'Venda cadastrada com sucesso')
                return redirect('index')
            else:
                messages.error(request, 'Estoque do produto esgotado!')

    return render(request, 'crm/sales/new_sale.html',{'form': form})

def edit_sale(request, sale_id):
    sale = Sale.objects.get(id=sale_id)
    
    form = SaleForm(instance=sale)

    if request.method == 'POST':
        form = SaleForm(request.POST, instance=sale)
        
        if form.is_valid():
            form.save()
            messages.success(request, 'Venda editada com sucesso')
            return redirect('index')
        
    return render(request, 'crm/sales/edit_sale.html', {'form': form, 'sale_id': sale_id})

def delete_sale(request, sale_id):
    sale = Sale.objects.get(id=sale_id)
    sale.delete()
    messages.success(request, 'Venda excluída com sucesso')
    return redirect('index')