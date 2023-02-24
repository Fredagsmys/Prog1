from time import sleep
import destinations
import trafficComponents as tc

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
