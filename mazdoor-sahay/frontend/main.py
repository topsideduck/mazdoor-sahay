import logging

from colorama import Fore, Style
from flask import Flask, render_template, request
from flask_cors import CORS
from waitress import serve


app = Flask(__name__)
CORS(app)


# Logger custom formatter

class CustomFormatter(logging.Formatter):
    green = Fore.GREEN
    yellow = Fore.YELLOW
    red = Fore.RED
    bold_red = Style.BRIGHT + Fore.RED
    reset = Fore.RESET
    format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s (%(filename)s:%(lineno)d)"

    FORMATS = {
        logging.DEBUG: green + format + reset,
        logging.INFO: green + format + reset,
        logging.WARNING: yellow + format + reset,
        logging.ERROR: red + format + reset,
        logging.CRITICAL: bold_red + format + reset
    }

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt)
        return formatter.format(record)


# Initialise logger

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Initialise console logger

c_handler = logging.StreamHandler()
c_handler.setLevel(logging.DEBUG)
c_handler.setFormatter(CustomFormatter())
logger.addHandler(c_handler)

# Initialise file logger

f_handler = logging.FileHandler('routing.log')
f_handler.setLevel(logging.DEBUG)
f_handler.setFormatter(
    logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s (%(filename)s:%(lineno)d)"))
logger.addHandler(f_handler)


@app.after_request
def Log(response):
    # info = str(request.environ['HTTP_X_FORWARDED_FOR']) + "==" + str(request.endpoint) + "==" + str(response.status)
    info = f"{str(request.environ['HTTP_X_FORWARDED_FOR'])} {str(request.endpoint)} {str(response.status)}"
    logging.info(info)
    return response


@app.route('/')
def Home():
    return render_template('Community.html')


@app.route('/Register')
def Register():
    return render_template('Register.html')


@app.route('/Login')
def Login():
    return render_template('LoginPage.html')


@app.route('/Community')
def Community():
    return render_template('Community.html')


@app.route('/Profile')
def Profile():
    return render_template('ProfilePage.html')


@app.route('/Account')
def Account():
    return render_template('Account.html')


@app.route('/CreatePost')
def CreatePost():
    return render_template('CreatePost.html')


@app.route('/ViewPost')
def ViewPost():
    return render_template('PostComments.html')


@app.route('/Donations')
def Donations():
    return render_template('DonationsPage.html')


@app.route('/Jobs')
def Jobs():
    return render_template('Jobs.html')


if __name__ == "__main__":
    serve(app, host='0.0.0.0', port=5000)
