from time import sleep
import destinations
import trafficComponents as tc




'''   
class Vehicle:
    """Represents vehicles in traffic simulations"""

    def __init__(self, destination, borntime):
        self.destination = destination
        self.borntime = borntime
        
    def __str__(self):
        return self.destination
    def __repr__(self):
        return self.destination
class Lane:
    "Represents a lane with (possible) vehicles"
    def __init__(self, length):
        self.length = length
        self.lane = [None for x in range(length)]
        
        self.s = {}
    def __str__(self):
        newlane = []
        newlane.append('[')
        for x in self.lane:
            if x == None:
                newlane.append('.')
            else:
                newlane.append(x.destination)
        newlane.append(']')
        self.s = ''.join(newlane)
        return self.s
    
    def enter(self, vehicle):
        self.vehicle = vehicle
        self.lane[self.length-1] = vehicle
        
    def last_free(self):
        pass

    def step(self): 
        for i in range(1,self.length):
            if self.lane[i-1] == None:
                self.lane[i-1] = self.lane[i]
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
    
class Destinations:
    """ Generates a sequence of destinations (None, 'W', 'S') """

    def __init__(self):
        self._arrivals = (  # 0:52, 1:26, 2:22
            2, 2, 2, 2, 2, 1, 2, 2, 2, 1, 1, 2, 1, 2, 2, 2, 1, 2, 1, 1,
            2, 1, 1, 0, 2, 0, 0, 0, 0, 1, 2, 0, 0, 0, 1, 0, 0, 2, 0, 1,
            2, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1,
            0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 2, 0, 0,
            1, 2, 0, 1, 0, 2, 0, 2, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1)

        self._internal_time = 0
        self._total_cycle = len(self._arrivals)

    def step(self):
        ind = self._arrivals[self._internal_time]
        self._internal_time = (self._internal_time + 1) % len(self._arrivals)
        return 'W' if ind == 1 else 'S' if ind == 2 else None

class Light:
    """Represents a traffic light"""

    def __init__(self, period, green_period):
        self.period = period
        self.green_period = green_period
        self.clock = 0
    def __str__(self):
        if self.clock >= self.green_period and self.clock <= self.period:
            return '(R)'
        else:
            return '(G)'
    def __repr__(self):
        return self.__str__()

    def step(self):
        
        self.clock += 1
        self.clock = self.clock % self.period
        
    def is_green(self):
        if self.clock >= self.green_period and self.clock <= self.period:
            return False
        else:
            return True
'''

class TrafficSystem:
    """Defines a traffic system"""

    def __init__(self):
        self.length = 10
        self.period = 7
        self.green_period = 3
        self.time = 0
        self.Lane1 = tc.Lane(self.length)
        self.Lane2 = tc.Lane(self.length)
        self.Light = tc.Light(self.period,self.green_period)
        self.destinations = destinations.Destinations()
        self.queue = []
        
        
        
        
    def snapshot(self):
        print(f'Time step {self.time}\n{self.Lane1}{self.Light} {self.Lane2} {self.queue}')
       
    def step(self):
        self.time += 1
        self.Lane1.remove_first()
        self.Lane1.step()
        if self.Light.is_green():
            self.Lane1.enter(self.Lane2.get_first())
            self.Lane2.remove_first()
            
            
        self.Light.step()
        self.Lane2.step()
        dest = self.destinations.step()
        if dest != None:
            
            vehicle = tc.Vehicle(dest,self.time)
            self.queue.append(vehicle)
           
        if self.Lane2.lane[self.length-1] == None:
            self.Lane2.enter(self.queue[0])
            self.queue.pop(0)
            
            
    def in_system(self):
        pass

    def print_statistics(self):
        pass

def main():
    ts = TrafficSystem()
    for i in range(100):
        ts.snapshot()
        ts.step()
        sleep(0.1)
    print('\nFinal state:')
    ts.snapshot()
    print()
    ts.print_statistics()

main()
