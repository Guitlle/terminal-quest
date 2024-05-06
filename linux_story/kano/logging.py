class Logger:
    def debug(self, message):
        print("DEBUG", message)

    def error(self, message):
        print("ERROR", message)

    def info(self, message):
        print("INFO", message)

logger = Logger()

