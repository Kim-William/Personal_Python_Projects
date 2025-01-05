# Logging with Flask Production Example Code
from flask import Flask 
import datetime

app = Flask(__name__)

# Set debug mode to False for production
app.debug = False

if not app.debug:
    import logging
    # Specify the logging handler to use
    from logging.handlers import RotatingFileHandler  
    file_handler = RotatingFileHandler('server.log', maxBytes=2000, backupCount=10) 
    # Define the logging level
    app.logger.level = logging.INFO 
    # Register the handler with app.logger to enable logging
    app.logger.addHandler(file_handler)  

@app.route('/')
def home():
    time_now = datetime.datetime.now()
    time_now = time_now.strftime("%Y-%m-%d %H:%M:%S")
    app.logger.debug(f'{time_now} :: [Debug]Home Page !!')
    app.logger.info(f'{time_now} :: [Info]Home Page !!')
    app.logger.warning(f'{time_now} :: [Warning]Home Page !!')
    app.logger.error(f'{time_now} :: [Error]Home Page !!')
    app.logger.critical(f'{time_now} :: [Critical]Home Page !!')
    return "<h1>home</h1>"

@app.errorhandler(404)
def page_not_found(error):
    app.logger.error(error)
    return "<h1>404 Error</h1>", 404

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5555", debug=False)
