from abc import ABC, abstractmethod

# ---------------- Strategy Interface ----------------
class PaymentStrategy(ABC):

    @abstractmethod
    def pay(self, amount):
        pass


# ---------------- Concrete Strategies ----------------
class CashPayment(PaymentStrategy):

    def pay(self, amount):
        print(f"Roshani Bhapkar paid ₹{amount} using Cash.")


class UPIPayment(PaymentStrategy):

    def pay(self, amount):
        print(f"Roshani Bhapkar paid ₹{amount} using UPI.")


class DebitCardPayment(PaymentStrategy):

    def pay(self, amount):
        print(f"Roshani Bhapkar paid ₹{amount} using Debit Card.")


# ---------------- Context Class ----------------
class PaymentProcessor:

    def __init__(self, strategy):
        self.strategy = strategy

    # Change payment strategy dynamically
    def set_strategy(self, strategy):
        self.strategy = strategy

    # Process payment
    def process_payment(self, amount):
        self.strategy.pay(amount)


# ---------------- Main Program ----------------
processor = PaymentProcessor(CashPayment())

print("Library Fine Payment - Cash")
processor.process_payment(500)

print("\nChanging Payment Method to UPI")
processor.set_strategy(UPIPayment())
processor.process_payment(350)

print("\nChanging Payment Method to Debit Card")
processor.set_strategy(DebitCardPayment())
processor.process_payment(750)