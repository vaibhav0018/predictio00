import os
import sys
sys.path.append('/home/avaxpro/Desktop/prediction')  # Adjust the path to your project directory if necessary

from flask import Flask
from src.logger import logging
from src.exception import CustomException

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    try:
        raise Exception("we are testing our exception file")
    except Exception as e:
        custom_exception = CustomException(e, sys)
        logging.info(custom_exception.error_message)
        logging.info("we are testing our logging file")
        return "Welcome to ML vaibhav"

if __name__ == "__main__":
    app.run(debug=True)
#hii hwjad
