import logging
import threading
import time
import signal
import sys

def getLogger(service_name):
    # Set the debug level
    logging.basicConfig(level=logging.DEBUG)
    # Create a logger
    return logging.getLogger(service_name)


logger = getLogger('pythonservice')


class MainApp(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.kill_me = False
        signal.signal(signal.SIGTERM, self.sigterm_handler)

    def sigterm_handler(self, signal, frame):
        logger.debug('SIGTERM')
        self.stop()

    def run(self):
        self.kill_me = False

        logger.debug('Starting application....')

        cnt = 0

        while not self.kill_me:
            logger.debug(cnt)
            cnt += 1
            time.sleep(1)

        logger.debug('Stopping application....')

    def stop(self):
        self.kill_me = True


def main():
    logger.debug('Welcome!')
    
    app = MainApp()
    app.start()

    while app.isAlive():
        try:
            time.sleep(1)
        except KeyboardInterrupt:
            app.stop()
            break

if __name__ == '__main__':
    main()

