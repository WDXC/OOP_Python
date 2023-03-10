from Chapter_7.driver_timer import format_time
from event_driven_timer import Timer


class Repeater:
    def __init__(self):
        self.count = 0

    def __call__(self,timer):
        format_time("{now}: repeat {0}", self.count)
        self.count += 1
        timer.call_after(5, self)

timer = Timer()

timer.call_after(5, Repeater())
format_time("{now}: Starting")
timer.run()