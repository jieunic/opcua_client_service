import time, datetime

class LoggingTime:
    def start():
        st = time.time()
        return st
    def end():
        et = time.time()
        return et
    def total(start_timer, end_timer):
        ttl = start_timer+end_timer
        formatted= datetime.timedelta(seconds=ttl)
        return ttl