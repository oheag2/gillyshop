from django.shortcuts import get_object_or_404
from products.models import Product


def cart_contents(request):
    """
    ensures that the cart contents are abailable when rendering every page
    """
    
    cart = request.session.get('cart', {})
    
    cart_items = []
    total = 0
    product_count = 0
    item_total = 0
    product_quan = 0
    for id, quantity in cart.items():
        product = get_object_or_404(Product, pk=id)
        total += quantity * product.price
        product_quan = request.POST.get(product_quan)
        item_total += product_quan * product.price
        product_count += quantity
        cart_items.append({'id':id, 'quantity':quantity, 'product': product})
        
        
    return { 'cart_items': cart_items, 'total': total, 'product_count': product_count, 'item_total': item_total }
    
    
    
    
    
        