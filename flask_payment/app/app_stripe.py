#database functionality. Collection of info comprising: phone number(user), shipping address, credit card token from stripe

# from pymongo import MongoClient
# client = MongoClient('mongodb://dbmagic:znmagic2@ds036698.mongolab.com:36698/darksidemagic')

# REMEMBER TO DELETE PRACTICE DOCUMENTS ON MONGOLAB -- http://api.mongodb.org/python/current/tutorial.html

# db = client.darksidemagic

# data = {'user': '+17186121018', 
# 'shipping': ['12 Upper Phillimore Gardens', 'w8 7ha', 'London', 'UK'],
# 'stripe_INFO: 'xxxxx'
# }

# #user information is document containing data.
# result = db.user_information.insert_one(data)   (LATER, DATA.APPEND)

# db.user_information.find_one({'user': 'their number'}) returns dictionary.

import os
from flask import Flask, render_template, request
import stripe
# KEYS TAKEN OUT

 
# stripe_keys = {
#   'secret_key': os.environ['SECRET_KEY'],
#   'publishable_key': os.environ['PUBLISHABLE_KEY']
# }
#SHOULD USE OS.ENVIRON TO HIDE PUBLIC KEYS. FOR TESTING ITS OK NOT TO
#also have to get my own keys from stripe dashboard

data = {}

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
	
 	token = request.form['stripeToken']
 	customer = stripe.Customer.create(
        source = token,
        description = '{{customer}} #their number',
        metadata = {'address': 'etc'}	#'shipping info'
    )
	

	# Save the customer ID in your database so you can use it later
	#save_stripe_customer_id(user, customer.id)
	# Later...
	#customer_id = get_stripe_customer_id(user)

	stripe.Customer.retrieve(customer.id)
	try:
		stripe.Charge.create(
		customer=customer.id, #or customer_id??,
		amount=200*100,
		#source = token,
		currency='usd',
		description='Amazin Charge'
	)
	except stripe.error.CardError, e:
		pass
 	print customer.metadata
 	return render_template('charge_stripe.html')
 
if __name__ == '__main__':
  app.run(debug=True)





