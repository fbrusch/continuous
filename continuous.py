from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from subprocess import call
from os.path import abspath
from argh import command, dispatch_command, arg
import time

wrap_open = "_"
wrap_close = "_"

def is_wrapped(s):
    return s[0] == wrap_open and s[-1:] == wrap_close

def unwrap(s):
    return s[1:-1]

class ContinuousHandler(FileSystemEventHandler):

    def __init__(self, args):
        self.watchlist = []
        self.args = []
        for a in args:
            if is_wrapped(a):
                ua = unwrap(a)
                self.watchlist.append(abspath(ua))
                self.args.append(ua)
            else:
                self.args.append(a)
        print "watchlist:"
        print self.watchlist

    def on_any_event(self, event):
        if event.src_path in self.watchlist:
            print event
            call(self.args)

@arg ("--call-on-startup", default = True)
@arg("command", nargs="+")
def continuous(args):
    call_on_startup = args.call_on_startup
    args = args.command
    print "args: "
    print args
    observer = Observer()
    handler = ContinuousHandler (args)
    observer.schedule(handler, '.', recursive = True)
    if call_on_startup:
        call(handler.args)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

def entry():
    dispatch_command(continuous)


if __name__ == '__main__':
    dispatch_command(continuous)
