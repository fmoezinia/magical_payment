# Set your secret key: remember to change this to your live secret key in production
# See your keys here https://dashboard.stripe.com/account/apikeys
stripe.api_key = "sk_test_azDI1jLdKJ9QEi7HeS78xcS8"

# Get the credit card details submitted by the form
token = request.POST['stripeToken']

# Create a Customer
customer = stripe.Customer.create(
    source=token,
    description="Example customer"
)

# Charge the Customer instead of the card
stripe.Charge.create(
    amount=1000, # in cents
    currency="gbp",
    customer=customer.id
)

# Save the customer ID in your database so you can use it later
save_stripe_customer_id(user, customer.id)

# Later...
customer_id = get_stripe_customer_id(user)

stripe.Charge.create(
    amount=1500, # £15.00 this time
    currency="gbp",
    customer=customer_id
)