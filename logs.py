import sys
sys.path.append('/home/avaxpro/Desktop/prediction')  # Adjust the path to your project directory if necessary

from flask import Flask
from src.logger import logging

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    logging.info("Logging a message from Flask application")
    return "Welcome to ML vaibhav"

if __name__ == "__main__":
    app.run(debug=True)
