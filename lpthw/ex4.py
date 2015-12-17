#var
#well this is the cars
cars = 100
#and that's how many people can be at the car 
space_in_a_car = 4.0
#drivers
drivers = 30
#passengers
passengers = 90
#no driver - no ride
cars_not_driven = cars - drivers
#if drivers < cars only!
cars_driven = drivers
#how many people can ride all cars
carpool_capacity = cars_driven * space_in_a_car
#to transport N passengers we need put them into the cars in such "capacity"
average_passengers_per_car = passengers / cars_driven

print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."

