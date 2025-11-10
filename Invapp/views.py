from django.shortcuts import  render, redirect
from .forms import ProductForm
from .models import Product

# Home page view
def home_view(request):
    return render(request, 'Invapp/home.html')

# Create product view
# Handles product creation with form validation and redirection
def product_create_view(request):   
        form = ProductForm()  # Bind data from request POST
        if request.method == 'POST':
            form = ProductForm(request.POST)
            if form.is_valid():
                form.save()  # Save new product
                return redirect('product_list')  # Redirect to product list after saving
        return render(request, 'Invapp/product_form.html', {'form': form})
# List products view
# Fetches all products and renders the list template
def product_list_view(request):
    products = Product.objects.all()  # Query all products from DB
    return render(request, 'Invapp/product_list.html', {'products': products})

# Update product view
# Fetches a product by ID, updates it via form, and redirects to list page
def product_update_view(request, product_id):
    product = Product.objects.get(product_id=product_id)
    form = ProductForm()  # Retrieve product or 404
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)  # Bind data to existing product
        if form.is_valid():
            form.save()  # Save updates
            return redirect('product_list')  # Redirect after update
    return render(request, 'Invapp/product_form.html', {'form': form})  # Reuse form template

# Delete View
# deletes a product by id and redirects to list page
def product_delete_view(request, product_id):
    product =Product.objects.get(product_id=product_id)
    if request.method == 'POST':
            product.delete()
            return redirect('product_list')
    return render(request, 'Invapp/product_confirm_delete.html', {'product': product})
