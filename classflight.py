class Flight():
    def __init__(self,capacity):
        self.capacity=capacity
        self.passengers=[]

    def add_passenger(self,name):
        if not self.available_seats():
            return False
        self.passengers.append(name)
        return True

    def available_seats(self):
        return self.capacity-len(self.passengers)

flight=Flight(3)

people=['Jhon','Mark','Brock','Rock','ortan']
for person in people:
    if flight.add_passenger(person):
        print(f"{person} has successfully booked the flight.")
    else:
        print(f"No available seats for {person}")