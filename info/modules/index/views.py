from flask import current_app
from flask import session

from info.modules.index import index_blu


@index_blu.route('/')
def index():
    session["name"] = "nima"
    # logging.debug("This is a debug log.")
    # logging.info("This is a info log.")
    # logging.warning("This is a warning log.")
    # logging.error("This is a error log.")
    # logging.critical("This is a critical log.")
    current_app.logger.debug('debug')
    current_app.logger.error('视图函数可以正常运行')
    return 'index'
