"""Let's use two examples to understand class variables and instance variables."""


class CountInstances:
    num_instances = 0

    def __init__(self):
        self.__class__.num_instances += 1  # increments every time the class is initiated


class CountBuggyInstance:
    num_instances = 0

    def __init__(self):
        self.num_instances += 1  # does not increment
