import os

import stripe
from flask import Flask, jsonify, render_template, request


app = Flask(__name__)

stripe_keys = {
  'secret_key': 'ENTER_YOUR_SECRET_KEY',
  'publishable_key': 'ENTER_YOUR_PUBLICATION_KEY'
}

stripe.api_key = stripe_keys['secret_key']


@app.route('/')
def index():
    return render_template('login.html')


@app.route('/payment')
def payment():
    return render_template('index.html', key=stripe_keys['publishable_key'])


@app.route('/charge', methods=['POST'])
def charge():
    try:
        amount = 500   # amount in cents
        customer = stripe.Customer.create(
            email='sample@customer.com',
            source=request.form['stripeToken']
        )
        stripe.Charge.create(
            customer=customer.id,
            amount=amount,
            currency='usd',
            description='Flask Charge'
        )
        return render_template('classifier.html', amount=amount)
    except stripe.error.StripeError:
        return render_template('error.html')


if __name__ == '__main__':
    app.run()
