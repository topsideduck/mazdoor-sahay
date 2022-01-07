from flask import Flask, render_template, request
from flask_cors import CORS
from waitress import serve
import logging
from datetime import datetime, date
import requests

app = Flask(__name__)
CORS(app)
logging.basicConfig(filename='routing.log', level=logging.DEBUG)


@app.after_request
def Log(response):
    today = date.today()
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    d1 = today.strftime("%d/%m/%Y")
    logging.info(d1 + "==" + current_time + "==" + str(request.environ['HTTP_X_FORWARDED_FOR']) + "==" + str(
        request.endpoint) + "==" + str(response.status))
    return response


@app.route('/Login')
def Login():
    return render_template('AdminLogin.html')


@app.route('/AddDonations')
def Donation():
    return render_template('AddDonation.html')


if __name__ == "__main__":
    serve(app, host='0.0.0.0', port=5000)
