import os
from flask import Flask, render_template, request
import stripe
PUBLISHABLE_KEY= 'pk_test_peLePyIXpcJWprVkixSOR99J' 
SECRET_KEY= 'sk_test_azDI1jLdKJ9QEi7HeS78xcS8'

 
# stripe_keys = {
#   'secret_key': os.environ['SECRET_KEY'],
#   'publishable_key': os.environ['PUBLISHABLE_KEY']
# }
#SHOULD USE OS.ENVIRON TO HIDE PUBLIC KEYS. FOR TESTING ITS OK NOT TO

 
stripe_keys = {
  'secret_key': SECRET_KEY,
  'publishable_key': PUBLISHABLE_KEY
}
 
stripe.api_key = stripe_keys['secret_key']
 
app = Flask(__name__)
 
@app.route('/')
def index():
  return render_template('index_stripe.html', key=stripe_keys['publishable_key'])
 
@app.route('/charge', methods=['POST'])
def charge():
	amount = 500
 
 	customer = stripe.Customer.create(
        email='customer@example.com',
        card=request.form['stripeToken']
    )
 
 	charge = stripe.Charge.create(
        customer=customer.id,
        amount=amount,
        currency='usd',
        description='Flask Charge'
    )
 
 	return render_template('charge_stripe.html', amount=amount)
 
if __name__ == '__main__':
  app.run(debug=True)