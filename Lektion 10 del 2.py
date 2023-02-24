

from statistics import mean, median
from time import sleep
import destinations
import trafficComponents as tc



class TrafficSystem:
    """Defines a traffic system"""

    def __init__(self):
        self.lanelength = 11
        self.lanews = 8
        self.period = 14
        self.west_green = 6
        self.south_green = 4
        self.time = 0
        self.Lane_south = tc.Lane(self.lanews)
        self.Lane_west = tc.Lane(self.lanews)
        self.Lane = tc.Lane(self.lanelength)
        self.Light_west = tc.Light(self.period,self.west_green)
        self.Light_south = tc.Light(self.period,self.south_green)
        self.destinations = destinations.Destinations()
        self.queue = []
        self.agew = []
        self.ages = []
        self.blocked = 0
        self.queuetime = 0
        self.nr_vehicles = 0
        
        
    def snapshot(self):
        print(f'Time step {self.time}\n{self.Light_west}{self.Lane_west} {self.Lane} {self.queue}\n{self.Light_south}{self.Lane_south}')
       
    def step(self):
        if self.Light_south.is_green():
            if self.Lane_south.get_first() != None:
                self.ages.append(self.time - self.Lane_south.get_first().borntime)
            self.Lane_south.remove_first()
            
        if self.Light_west.is_green():
            if self.Lane_west.get_first() != None:
                self.agew.append(self.time - self.Lane_west.get_first().borntime)
            self.Lane_west.remove_first()
            
        self.Lane_west.step()
        self.Lane_south.step()
        if self.Lane.get_first() != None:
            
            if self.Lane.get_first().destination == 'W':
                if self.Lane_west.last_free():
                    self.Lane_west.enter(self.Lane.get_first())
                    self.Lane.remove_first()
                else:
                    self.blocked += 1
            elif self.Lane.get_first().destination == 'S':
                if self.Lane_south.last_free():
                    self.Lane_south.enter(self.Lane.get_first())
                    self.Lane.remove_first()
                else:
                    self.blocked += 1

        self.Lane.step()
        if self.queue != []:    # räknar antalet tidssteg som det finns fordon i kön
            self.queuetime += 1
        dest = self.destinations.step()
        if dest != None:
            
            vehicle = tc.Vehicle(dest,self.time)
            self.queue.append(vehicle)
            self.nr_vehicles += 1
        
        if self.Lane.last_free():
            if self.queue != []:
                self.Lane.enter(self.queue[0])
                self.queue.pop(0)
                
        
            
        self.Light_west.step()
        self.Light_south.step()        
        self.time += 1
        
        
            
    def in_system(self):
        pass

    def print_statistics(self):
        print(f'Statistics after {timesteps} timesteps:\n')
        self.ages = sorted(self.ages,reverse = True)
        self.agew = sorted(self.agew,reverse = True)
        number_in_all_lanes = self.Lane.number_in_lane() + self.Lane_west.number_in_lane() + self.Lane_south.number_in_lane()
        print('Created vehicles:'.ljust(20),self.nr_vehicles)
        print('In system:'.ljust(20),number_in_all_lanes)
        print()
        print('At exit'.ljust(20), 'west'.ljust(20) ,'south')
        print('Vehicles out:'.ljust(20), len(self.agew),''.ljust(17), len(self.ages))
        print('Minimal time:'.ljust(20),self.agew[0],''.ljust(17),self.ages[0])
        print('Maximal time:'.ljust(20),self.agew[-1],''.ljust(17),self.ages[-1])
        print('Mean time:'.ljust(20),round(mean(self.agew),1),''.ljust(15),round(mean(self.ages),1))
        print('Median:'.ljust(20),median(self.agew),''.ljust(17),median(self.ages))
        print()
        print('Blocked:'.ljust(20),float(self.blocked*100//self.time),'%')
        print('Queue:'.ljust(20),float(self.queuetime*100//self.time),'%')
        
timesteps = 100

def main():
    ts = TrafficSystem()
    for i in range(timesteps):
        ts.snapshot()
        ts.step()
        sleep(0.1)
    print('\nFinal state:')
    ts.snapshot()
    print()
    ts.print_statistics()

main()
