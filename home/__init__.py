def homepage(request):
    cart =request.session.get('cart', {})
    total_items = sum(cart.values())
    return render(request, 'homepage.html', {'total_items': total_items})


def add-to-cart{request, item_id}:
cart = request.session.get('cart'. {})
cart[item_id] = cart.get(item_id, 0) + 1
request.session['cart'] = cart
return redirect('homepage')