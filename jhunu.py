import time

from sched import scheduler


print('START:', time.time())


class Scheduler:
    client = scheduler(time.time, time.sleep)

    def __init__(self) -> None:
        self.client.run()

    def _call(self, *args, **kwargs):
        print('EVENT:', time.time(), *args, **kwargs)


# # first event with delay of
# # 1 second
# e1 = scheduler.enter(1, 1, print_event, ('1 st', ))

# # second event with delay of
# # 2 seconds
# e1 = scheduler.enter(2, 1, print_event, (' 2nd', ))
