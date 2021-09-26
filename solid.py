from abc import ABC, abstractmethod


class Order:
    """Order a product"""

    items = []
    quantities = []
    prices = []
    status = "open"

    def add_item(self, name, quantity, price):
        """Add Item to the order list"""

        self.items.append(name)
        self.quantities.append(quantity)
        self.prices.append(price)

    def total_price(self):
        """Calculate total price"""

        total = 0
        for i in range(len(self.prices)):
            total += self.quantities[i] * self.prices[i]

        return total


class PaymentProcessor(ABC):
    """Abstract class for payment processor"""

    @abstractmethod
    def pay(self, order):
        pass


class PaymentProcessor_SMS(ABC):
    """Abstract class for payment processor"""

    @abstractmethod
    def pay(self, order):
        pass

    @abstractmethod
    def sms_verification(self, otp):
        pass


class CreditPaymentProcessor(PaymentProcessor):
    """Process credit payment"""

    def __init__(self, security_code):
        self.security_code = security_code

    def pay(self, order):
        print("Processing Credit Card")
        print(f"Verifying security code: {self.security_code}")
        order.status = "paid"


class DebitPaymentProcessor(PaymentProcessor):
    """Process credit payment"""

    def __init__(self,security_code):
        self.security_code = security_code

    def pay(self, order):
        print("Processing Debit Card")
        print(f"Verifying security code: {self.security_code}")
        order.status = "paid"


class PaypalPaymentProcessor(PaymentProcessor_SMS):
    """Process credit payment"""

    def __init__(self, email_address):
        self.email_address = email_address
        self.verified = False

    def pay(self, order):
        print("Processing Paypal Card")
        print(f"Verifying email address: {self.email_address}")
        order.status = "paid"

    def sms_verification(self, otp):
        print(f"Verifying SMS code: {otp}")
        self.verified = True


order = Order()
order.add_item("Monitor", 1, 10000)
order.add_item("Mouse Pad", 2, 1500)

print(order.total_price())
pay_processor = CreditPaymentProcessor("654623")
pay_processor2 = PaypalPaymentProcessor("nuruddi@emai.com")
pay_processor.pay(order)
pay_processor2.pay(order)
pay_processor2.sms_verification("54876")