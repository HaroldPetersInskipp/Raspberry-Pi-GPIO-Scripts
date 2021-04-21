import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from gpiozero import LED

usbdeviceled = LED(21) #replace this number if your led is connected to a different pin.

class Watcher:
    DIRECTORY_TO_WATCH = "/path/to/my/directory" #replace this with the path to the folder or drive you want to monitor.

    def __init__(self):
        self.observer = Observer()

    def run(self):
        event_handler = Handler()
        self.observer.schedule(event_handler, self.DIRECTORY_TO_WATCH, recursive=True)
        self.observer.start()
        try:
            while True:
                time.sleep(5)
        except:
            self.observer.stop()
            print "Error"

        self.observer.join()


class Handler(FileSystemEventHandler):

    @staticmethod
    def on_any_event(event):
        if event.is_directory:
            return None

        elif event.event_type == 'created':
            # Take any action here when a file is first created.
            usbdeviceled.on()
            sleep(0.5)
            usbdeviceled.off()

        elif event.event_type == 'modified':
            # Take any action here when a file is modified.
            usbdeviceled.on()
            sleep(0.5)
            usbdeviceled.off()


if __name__ == '__main__':
    w = Watcher()
    w.run()