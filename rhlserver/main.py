__author__ = 'Rahul Vishwakarma'

import os
from bottle import run

# import DataService web services
import ConfigParser
import DataService

# Initializing the configuration
config = ConfigParser.ConfigParser()
config.read('config.cfg')
hostname = config.get("server", "host")
portnum = config.get("server", "port")

if __name__ == '__main__':
    port = int(os.environ.get('PORT', portnum))
    run(host=hostname, port=port, debug=True)