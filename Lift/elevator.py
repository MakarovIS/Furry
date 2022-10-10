class Elevator:
    def __init__(self, maximum_floors, maximum_cargo):
        self.elevator_maximum_floors = maximum_floors
        self.elevator_maximum_cargo = maximum_cargo
        self.elevator_position = 1
        self.elevator_cargo = 0

class Passenger:
    def __init__(self, cargo, position, floor):
        if cargo < elevator.elevator_maximum_cargo:
            self.passenger_cargo = cargo
            elevator.elevator_cargo = elevator.elevator_cargo + cargo
        else:
            print("Вес пассажира не соответствует условиям лифта")
            self.passenger_cargo = 0
        if (position <= elevator.elevator_maximum_floors) and (position >= 1):
            self.passenger_position = position
        else:
            print("Местонахождения пассажира не соответствует условиям лифта")
            self.passenger_position = 0
        if (floor <= elevator.elevator_maximum_floors) and (floor >= 1):
            self.passenger_needed_floor = floor
        else:
            print("Нужный этаж не соответствует условиям лифта")
            self.passenger_needed_floor = 0

def elevator_move(first_way, second_way):
    if (first_way != 0) and (second_way != 0) and (passenger.passenger_cargo != 0):
        elevator.elevator_position = first_way
        print("Лифт остановился на", elevator.elevator_position, "этаже, пассажир зашел в лифт")
        elevator.elevator_position = second_way
        print("Лифт остановился на", elevator.elevator_position, "этаже, пассажир вышел из лифта")
        elevator.elevator_cargo = elevator.elevator_cargo - passenger.passenger_cargo
        
elevator = Elevator(16,300)
passenger = Passenger(60,1,12)
elevator_move(passenger.passenger_position, passenger.passenger_needed_floor)
