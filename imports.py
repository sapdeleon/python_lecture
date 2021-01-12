import classes

people = ["Harry", "Ron", "James", "Dave"]

# create new Flight object with 3 maximum capacity
flight = classes.Flight(3);

for person in people:
    if flight.add_passenger(person):
        print(f"Added {person} to flight successfully!")
    else:
        print(f"Sorry, no available seat for {person}.")