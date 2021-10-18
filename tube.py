from python import name

import time
import sys

fname = input("type your name: ")

class Flight():
    # Mehod to create a new flight with given capacity
    def __init__(self, capacity):
     self.capacity = capacity
     self.passengers = []

    def add_passenger(self, name):
        if not self.open_seats():
          return False
        self.passengers.append(name)
        return True

    def open_seats(self):
        return self.capacity - len(self.passengers)

# flight with up to 3 peoples
flight = Flight(3)

people = ["Harry", "Ron", "Hermonie"]
people.append(name)
people.append(fname)
people.sort

for person in people:
    if flight.add_passenger(person):
        print(f"added {person} to Flight succesfully")
    else:
        print(f"{person} has no avaivable seats in the Flight")

# attemp to count memeers in people list (4)
print(f'flight is taking off')
time.sleep(10)
print(f"flight taked of Succesfully")
sys.exit(0)
