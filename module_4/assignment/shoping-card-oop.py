class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    def __str__(self):
        return f"{self.name} - {self.price}"

class CartItem:
    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity

    def total_price(self):
        return self.product.price * self.quantity
    
    def __str__(self):
        return f"{self.product} - {self.quantity}"

class Cart:
    def __init__(self, customer):
        self.customer = customer
        self.items = []

    def add_item(self, product, quantity):
        self.items.append(CartItem(product, quantity))

    def remove_item(self, product):
        self.items = [item for item in self.items if item.product != product]

    def total_price(self):
        return sum(item.total_price() for item in self.items)
    
    def __str__(self):
        return f"{self.customer.name} - {self.total_price()} - {', '.join(str(item) for item in self.items)}"

class Customer:
    def __init__(self, name, email):
        self.name = name
        self.email = email
    
    def __str__(self):
        return f"{self.name} - {self.email}"

from abc import ABC, abstractmethod
class Payment(ABC):
    @abstractmethod
    def pay(self):
        pass

class CreditCardPayment(Payment):
    def __init__(self, card_number, card_holder, expiry_date):
        self.card_number = card_number
        self.card_holder = card_holder
        self.expiry_date = expiry_date
    
    def pay(self, amount):
        print(f"Payment of ${amount} made with card {self.card_number}")

class CashPayment(Payment):
    def pay(self, amount):
        print(f"Payment of ${amount} made with cash")


if __name__ == '__main__':
    customer = Customer('Francis Rudra D Cruze', 'francisrudra@gmail.com')
    cart = Cart(customer)
    product1 = Product('Laptop', 1000)
    product2 = Product('Mouse', 20)
    product3 = Product('Keyboard', 50)
    cart.add_item(product1, 2)
    cart.add_item(product2, 5)
    cart.add_item(product3, 1)
    print(cart)
    cart.remove_item(product1)
    print(cart)
    print(cart.total_price())

    payment = CreditCardPayment('1234 5678 9012 3456', 'Francis Rudra D Cruze', '12/23')
    payment.pay(cart.total_price())
    payment = CashPayment()

    # payment.pay(cart.total_price())
    print(cart)
    print(customer)