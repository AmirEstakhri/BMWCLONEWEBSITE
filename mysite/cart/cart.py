from main.models import Product, Profile

class Cart:
    def __init__(self, request):
        self.session = request.session
        self.request = request
        cart = self.session.get('session_key')

        if cart is None:  # Initialize if cart is not present
            cart = self.session['session_key'] = {}

        self.cart = cart

    def add(self, product, quantity):
        product_id = str(product.id)
        if product_id in self.cart:
            self.cart[product_id] += int(quantity)
        else:
            self.cart[product_id] = int(quantity)

        self.session.modified = True
        self._update_user_cart()

    def _update_user_cart(self):
        if self.request.user.is_authenticated:
            current_user = Profile.objects.filter(user=self.request.user).first()
            if current_user:
                carty = str(self.cart).replace("'", "\"")
                current_user.old_cart = carty  # Update the old_cart field
                current_user.save()  # Save changes to the Profile

    def cart_total(self):
        total = 0
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)

        for product in products:
            qty = self.cart[str(product.id)]
            if product.is_sales and product.sales_price is not None:  # Use sales_price
                total += product.sales_price * qty
            else:
                total += product.price * qty

        return total

    def get_items(self):
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        return [{'product': product, 'quantity': self.cart[str(product.id)]} for product in products]

    def __len__(self):
        return sum(self.cart.values())

    def update(self, product, quantity):
        product_id = str(product.id)
        self.cart[product_id] = int(quantity)
        self.session.modified = True
        self._update_user_cart()

    def delete(self, product):
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
        self.session.modified = True
        self._update_user_cart()

    def get_prods(self):
        product_ids = self.cart.keys()
        return [Product.objects.get(id=prod_id) for prod_id in product_ids]

    def get_quants(self):
        # Returns the quantities of products in the cart
        return {product_id: quantity for product_id, quantity in self.cart.items()}
