class Logger:
    def debug(self, message):
        # print("DEBUG", message)
        pass

    def error(self, message):
        print("ERROR", message)

    def info(self, message):
        print("INFO", message)

logger = Logger()

