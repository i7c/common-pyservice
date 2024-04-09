import time


class Time(object):
    def __init__(self):
        self.timers = {}

    def now(self, tnow=None):
        if tnow:
            return tnow
        return time.time()

    def start_timer(self, timer):
        now = self.now()
        self.timers[timer] = now
        return now

    def stop_timer(self, timer):
        now = self.now()
        if timer not in self.timers:
            raise ValueError(f'Trying to stop timer {timer}, but it was never started.')
        start = self.timers[timer]
        del self.timers[timer]
        return now - start

    def elapsed_timer(self, timer):
        now = self.now()
        if timer not in self.timers:
            raise ValueError(f'Trying to peek at timer {timer}, but it was never started.')
        start = self.timers[timer]
        return now - start


class MockTime(object):
    def __init__(self):
        self.time = None
        self.oneshot = False

    def set_time(self, t):
        if not self.time:
            self.oneshot = True
        self.time = t

    def release(self):
        self.oneshot = False

    def freeze(self):
        self.oneshot = True

    def _oneshot_now(self):
        if self.time:
            t = self.time
            self.time = None
            return t
        else:
            raise ValueError("Mock time is not set, use set_time()")

    def now(self, tnow=None):
        if tnow:
            return tnow

        if self.oneshot:
            return self._oneshot_now()

        if not self.time:
            self.time = time.time()
            return self.time

        # Advance roughly 1 second
        self.time += 0.9965436173

        return self.time
