class Vehicle:

    def __init__(self, destination, borntime):
        self.destination = destination
        self.borntime = borntime

    def __str__(self):
        return self.destination

    def __repr__(self):
        return self.destination


class Lane:

    def __init__(self, length):
        self.length = length
        self.lane = [None for x in range(length)]

        self.s = {}

    def __str__(self):
        newlane = []
        newlane.append('[')
        for x in range(len(self.lane)):
            if self.lane[x] == None:
                newlane.append('.')
            else:
                newlane.append(self.lane[x].destination)
        newlane.append(']')
        self.s = ''.join(newlane)
        return self.s

    def enter(self, vehicle):
        self.lane[-1] = vehicle

    def last_free(self):
        if self.lane[-1] == None:
            return True
        else:
            return False

    def step(self):
        for i in range(1, self.length):
            if self.lane[i - 1] == None:
                self.lane[i - 1] = self.lane[i]
                self.lane[i] = None

    def get_first(self):
        return self.lane[0]

    def remove_first(self):
        if self.lane[0] == None:
            return None
        first = self.lane[0]
        self.lane[0] = None
        out = first.destination
        out2 = first.borntime
        return f'Vehicle({out}, {out2})'

    def number_in_lane(self):
        number = 0
        for x in self.lane:
            if x != None:
                number += 1
        return number


class Light:

    def __init__(self, period, green_period):
        self.period = period
        self.green_period = green_period
        self.clock = 0

    def __str__(self):
        if self.clock >= self.green_period and self.clock <= self.period:
            return '(R)'
        else:
            return '(G)'

    def step(self):

        self.clock += 1
        self.clock = self.clock % self.period

    def is_green(self):
        if self.clock >= self.green_period and self.clock <= self.period:
            return False
        else:
            return True
