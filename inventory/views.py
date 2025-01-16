from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Product, Supplier, SaleOrder, StockMovement
from .forms import ProductForm, SupplierForm, SaleOrderForm, StockMovementForm
from decimal import Decimal
from datetime import datetime

def home(request):
    return render(request, 'inventory/home.html')

def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save(commit=False)
            if Product.objects.filter(name=product.name).exists():
                messages.error(request, 'Product with this name already exists.')
            else:
                product.save()
                messages.success(request, 'Product added successfully.')
                return redirect('list_products')
    else:
        form = ProductForm()
    return render(request, 'inventory/add_product.html', {'form': form})

def list_products(request):
    products = Product.objects.all()
    return render(request, 'inventory/list_products.html', {'products': products})

def add_supplier(request):
    if request.method == 'POST':
        form = SupplierForm(request.POST)
        if form.is_valid():
            supplier = form.save(commit=False)
            if Supplier.objects.filter(email=supplier.email).exists():
                messages.error(request, 'Supplier with this email already exists.')
            else:
                supplier.save()
                messages.success(request, 'Supplier added successfully.')
                return redirect('list_suppliers')
    else:
        form = SupplierForm()
    return render(request, 'inventory/add_supplier.html', {'form': form})

def list_suppliers(request):
    suppliers = Supplier.objects.all()
    return render(request, 'inventory/list_suppliers.html', {'suppliers': suppliers})

def add_stock_movement(request):
    if request.method == 'POST':
        form = StockMovementForm(request.POST)
        if form.is_valid():
            movement = form.save(commit=False)
            product = movement.product
            if movement.movement_type == 'In':
                product.stock_quantity += movement.quantity
            else:
                if product.stock_quantity < movement.quantity:
                    messages.error(request, 'Insufficient stock.')
                    return render(request, 'inventory/add_stock_movement.html', {'form': form})
                product.stock_quantity -= movement.quantity
            product.save()
            movement.movement_date = datetime.now()
            movement.save()
            messages.success(request, 'Stock movement recorded successfully.')
            return redirect('list_products')
    else:
        form = StockMovementForm()
    return render(request, 'inventory/add_stock_movement.html', {'form': form})

def create_sale_order(request):
    if request.method == 'POST':
        form = SaleOrderForm(request.POST)
        if form.is_valid():
            sale_order = form.save(commit=False)
            product = sale_order.product
            if product.stock_quantity < sale_order.quantity:
                messages.error(request, 'Insufficient stock.')
            else:
                sale_order.total_price = product.price * Decimal(sale_order.quantity)
                sale_order.sale_date = datetime.now()
                sale_order.save()
                product.stock_quantity -= sale_order.quantity
                product.save()
                messages.success(request, 'Sale order created successfully.')
                return redirect('list_sale_orders')
    else:
        form = SaleOrderForm()
    return render(request, 'inventory/create_sale_order.html', {'form': form})

def cancel_sale_order(request, order_id):
    sale_order = get_object_or_404(SaleOrder, id=order_id)
    if sale_order.status == 'Pending':
        sale_order.status = 'Cancelled'
        sale_order.save()
        product = sale_order.product
        product.stock_quantity += sale_order.quantity
        product.save()
        messages.success(request, 'Sale order cancelled successfully.')
    else:
        messages.error(request, 'Cannot cancel a completed or already cancelled order.')
    return redirect('list_sale_orders')

def complete_sale_order(request, order_id):
    sale_order = get_object_or_404(SaleOrder, id=order_id)
    if sale_order.status == 'Pending':
        sale_order.status = 'Completed'
        sale_order.save()
        messages.success(request, 'Sale order completed successfully.')
    else:
        messages.error(request, 'Cannot complete a cancelled or already completed order.')
    return redirect('list_sale_orders')

def list_sale_orders(request):
    sale_orders = SaleOrder.objects.all()
    return render(request, 'inventory/list_sale_orders.html', {'sale_orders': sale_orders})

def check_stock_levels(request):
    products = Product.objects.all()
    return render(request, 'inventory/check_stock_levels.html', {'products': products})

