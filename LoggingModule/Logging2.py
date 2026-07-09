import logging


logging.basicConfig(level=logging.CRITICAL)
logging.debug("Hello this is a debug.") 
logging.warning("Achtung!!!")
logging.critical("Wow")

logging.basicConfig(level=logging.INFO, force=True)  # Здесь чтобы изменить минимальный уровень логирования нужно добавлять force=True.
logging.debug("Hello this is a debug.") 
logging.warning("Achtung!!!")
logging.critical("Wow")
