class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    def __str__(self):
        return f"{self.name} has a price of {self.price}"

    def __repr__(self):
        return f"Product(name={self.name}, price={self.price})"


class User:
    def __init__(self, name, is_premium=False, is_admin=False):
        self.name = name
        self.__is_premium = is_premium
        self.__is_admin = is_admin

    @property
    def is_premium(self):
        return self.__is_premium

    @is_premium.setter
    def is_premium(self, premium):
        self.__is_premium = premium

    @property
    def is_admin(self):
        return self.__is_admin

    @is_admin.setter
    def is_admin(self, admin):
        self.__is_admin = admin

    def promote_to_premium(self, diff_user):
        if self.is_admin:
            diff_user.is_premium = True
            print(f"{diff_user.name} has been promoted to a premium user.")
        else:
            print(f"{self.name} cannot promote users to premium.")
    
    def promote_to_admin(self, diff_user):
        if self.is_admin:
            diff_user.is_admin = True
            print(f"{diff_user.name} has been promoted to admin.")
        else:
            print(f"{self.name} cannot promote users to admin.")


class ShoppingCart:
    def __init__(self, user):
        self.user = user
        self.cart_items = []

    def add_product(self, product):
        self.cart_items.append(product)
        print(f"Added {product.name} to {self.user.name}'s cart.")
    
    def remove_product(self, product):
        if product in self.cart_items:
            self.cart_items.remove(product)
            print(f"Removed {product.name} from {self.user.name}'s cart.")
        else:
            print(f"{product.name} not found in {self.user.name}'s cart.")

    def calculate_total_cost(self):
        total = sum(item.price for item in self.cart_items)
        return total
    
    def discount_10_percent(func):
        def wrapper(self):
            total = func(self)
            if self.user.is_premium:
                total *= 0.9  
            return total
        return wrapper

    @discount_10_percent
    def calculate_discounted_total(self):
        return self.calculate_total_cost()

    def generate_invoice(self):
        print(f"Invoice for {self.user.name}:")
        for item in self.cart_items:
            print(f"{item.name}: {item.price}")
        total_cost = self.calculate_discounted_total()
        print(f"Total cost: {total_cost}")



product1 = Product("Laptop", 1000)
product2 = Product("Headphones", 200)
product3 = Product("Mouse", 50)

 
admin_user = User("Kushal", is_admin=True)
regular_user = User("Ram")

 
admin_user.promote_to_premium(regular_user)
admin_user.promote_to_admin(regular_user)

 
shop_cart = ShoppingCart(regular_user)
shop_cart.add_product(product1)
shop_cart.add_product(product2)
shop_cart.remove_product(product3)   

shop_cart.generate_invoice()

admin_cart = ShoppingCart(admin_user)
admin_cart.add_product(product3)
admin_cart.generate_invoice()
 
another_user = User("Shyam")
shop2_cart = ShoppingCart(another_user)
shop2_cart.add_product(product1)
shop2_cart.generate_invoice()



 
