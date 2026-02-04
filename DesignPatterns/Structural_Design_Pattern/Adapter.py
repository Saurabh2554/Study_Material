"""
🔹 What is the Adapter Design Pattern?

1. The Adapter Pattern is a structural design pattern.

2. It allows two incompatible interfaces to work together without changing their existing code.

3. Think of it as a translator between two different systems.

👉 Intent: Convert the interface of a class into another interface clients expect.

🔹 Common Real-World Use Cases
1. Payment Gateway Integrations (Very Common)

Your system has a standard interface like PaymentProcessor.pay(amount).
Stripe, PayPal, Razorpay all have completely different SDKs and APIs.
You write an Adapter per provider to normalize them.

👉 Used in e-commerce platforms like Amazon, Flipkart, Shopify.

3. Cloud Storage SDKs
AWS S3, Google Cloud Storage, and Azure Blob Storage each have different APIs.
Your app defines a simple interface:

class StorageClient:
    def upload(self, file, path): pass
    def download(self, path): pass

Each cloud provider gets its own Adapter.
Business logic stays the same → swap providers easily.

👉 Used in Dropbox, Google Drive, SaaS apps supporting multi-cloud.

5. Legacy System Integration
Suppose your company has an old SOAP-based service, but your app expects REST/JSON.
You build a SOAP → REST Adapter.
Or vice versa, if a partner only accepts SOAP.

👉 Used in banking/insurance/healthcare, where legacy systems must co-exist.

4. Database Drivers
ORMs (like SQLAlchemy, Hibernate, Django ORM) act as adapters.
They adapt different DB drivers (Postgres, MySQL, SQLite) to a unified interface (.filter(), .save(), .update()).
Your app doesn’t care what DB is running under the hood.

👉 Used in enterprise backends to support multiple databases.
"""

from abc import ABC, abstractmethod

#Target Interface


class IPaymentProcessor(ABC):
    @abstractmethod
    def pay(self,amount:int)->None:pass

# Adaptee(from third party) already in use
class Paypal:
    def makePayment(self,amount:float): #earlier it was int
        print(f"{amount} Amount paid via Paypal.")


#Earlier we were using simply like
# PProcessor =  Paypal()
# PProcessor.makePayment(200)

"""
But there may be a situation arise where paypal stops accepting payment in int and asks us to send payment in dollar(double). 
Then in that case if we are using makePayment() at multiple places, 
we will need to change from int to double at each and every place.
"""

"""
In that case it would be better to make an adapter or say a translator which takes int from client, 
converts to double and then passes to makePayment().
Here we can not simply make changes to makePayment as it is a third party library.
"""

#Adapter/Translator
class PaypalAdaptor(IPaymentProcessor):
    def __init__(self, paypal:Paypal):
        self.paypal = paypal

    def pay(self,amount:int):
        self.paypal.makePayment(float(amount)) 





# If in future we extend our system to support Stripe then

class Stripe:
    def makePayment(self,amount:float): #accept amount in dollars
        print(f"{amount} dollar paid via stripe")

class StripeAdapter(IPaymentProcessor):
    def __init__(self, stripe:Stripe):
        self.stripe = stripe

    def pay(self, amount:float): #Accepts amount in ruppee
        amount_in_dollar = amount/93
        self.stripe.makePayment(amount_in_dollar)

class Client:
    @classmethod
    def main(cls, amount:int):
        #Payment via paypal
        # paymentAdapter = PaypalAdaptor(Paypal())
        # paymentAdapter.pay(amount)

        #Payment via stripe
        paymentAdapter = StripeAdapter(Stripe())
        paymentAdapter.pay(amount)


if __name__ == "__main__":
    Client.main(187)
            
